---
title: "Active Context Tasks"
description: "Design document for the Active Context Tasks framework"
status: implemented
creation-date: "2026-06-23"
authors: [ "@partiaga" ]
coaches: [ ]
dris: [ "@wortschi" ]
owning-stage: "~devops::ai platform"
participating-stages: []
toc_hide: true
---

## Overview

`ActiveContext::Task` is a framework for managing long-running, asynchronous operations within the ActiveContext system. It provides a structured way to define, execute, and track complex workflows that may involve multiple sequential or dependent steps.

This is designed to handle operations like embedding model switching, embeddings field creation and backfill, and metadata synchronization that require careful orchestration and error handling.

## Components

### Task Base Class (`ActiveContext::Task[1.0]`)

The abstract base class for all task implementations and defines the interface that all subclasses must follow.

The concrete class implementations define the actual logic of the task.

**Batched Tasks:**

Tasks can be marked as `batched!` to indicate they perform work in batches and may need multiple executions to complete. For batched tasks, `completed?` must be implemented to determine when all work is done.

**Example Task class implementations**

- `Ai::ActiveContext::Tasks::BackfillEmbeddings`: Generates embeddings for existing documents using a new embedding model.
- `Ai::ActiveContext::Tasks::SyncFeatureSettings`: Synchronizes feature settings with the embedding model configuration.

### Task Model (`Ai::ActiveContext::Task`)

The ActiveRecord model that persists task information.

**Database Schema:**

- `connection_id` - Foreign key to the vector store connection
- `depends_on_id` - Foreign key to the preceding task (for [task chains](#task-chains))
- `name` - The task class name
- `status` - Current execution status (`pending`, `in_progress`, `completed`, `failed`)
- `params` - JSON parameters passed to the task
- `retries_left` - Number of retry attempts remaining (default: 3)
- `started_at` - When execution began
- `completed_at` - When execution finished
- `error_message` - Error details if the task failed

### Task Dictionary (`ActiveContext::Task::Dictionary`)

The registry of defined task classes. This provides a singleton instance for global access.

```ruby
# Find a task class by name
task_class = ActiveContext::Task::Dictionary.instance.find_by_name('Ai::ActiveContext::Tasks::BackfillEmbeddings')

# Or use the shorthand
task_class = ActiveContext::Task::Dictionary.find_by_name('Ai::ActiveContext::Tasks::BackfillEmbeddings')

# Returns an array of task class objects that have been loaded
ActiveContext::Task::Dictionary.instance.tasks
```

### Task Service (`Ai::ActiveContext::TaskService`)

Creates and manages task chains.

- `create_task(task_class, params: {}, depends_on: nil)` - Create a single task
- `create_chain(*tasks_with_params)` - Create a sequence of dependent tasks

**Example Usage:**

```ruby
service = Ai::ActiveContext::TaskService.new
service.create_chain(
  [Ai::ActiveContext::Tasks::AddEmbeddingsField, { collection: 'code', field: 'embeddings_v2', dimensions: 768 }],
  [Ai::ActiveContext::Tasks::BackfillEmbeddings, { collection: 'code', field: 'embeddings_v2' }],
  [Ai::ActiveContext::Tasks::UpdateCollectionMetadata, { collection: 'code', metadata: {...} }]
)
```

### Task Worker (`Ai::ActiveContext::TaskWorker`)

The Sidekiq worker responsible for executing created tasks.

**Execution Flow:**

1. Worker finds the next processable task record
1. Instantiates the correct task object from the task record `name`
1. Marks task record as `in_progress`
1. Calls `execute!` on the task object
1. On success: marks task record as `completed`
1. On failure: see "Error handling" details below
1. If task is batched and not completed: re-enqueues worker
1. If no more processable tasks: worker exits

**Error Handling:**

- Catches exceptions during task execution
- For each failed execution, the number of retries is decreased and:
  - Task stays `in_progress` with one fewer retry; the cron worker picks it up on its next run
  - Task is marked as `failed` and cascades to dependents (if no retries left)

**Re-enqueueing Logic:**

- For batched tasks that aren't completed, worker re-enqueues to continue processing
- After a successful non-batched task, the worker exits; the cron-scheduled invocation picks up the next one

## Task Chains

Tasks can depend on other tasks through the `depends_on` relationship. A task only becomes processable when:

- Its status is `pending` or `in_progress`, AND
- Either it has no dependency, OR its dependency has a `completed` status

This creates a directed acyclic graph (DAG) of task execution.

## Task Execution Flow Summary

1. **Task Creation** - A service creates one or more tasks by using `TaskService`
1. **Dependency Resolution** - Tasks are chained through `depends_on` relationships
1. **Processable Selection** - The `Ai::ActiveContext::Task.processable` scope finds tasks ready to execute
1. **Worker Polling** - `TaskWorker` finds the next processable task through `Ai::ActiveContext::Task.current`
1. **Execution** - `TaskWorker` invokes the task's `execute!` method
1. **Status Transition** - Task status moves from pending → `in_progress` → `completed`/`failed`
1. **Dependent Execution** - Once a task completes, its dependents become processable
1. **Worker Re-enqueueing** - For batched tasks, the worker re-enqueues itself; otherwise the cron-scheduled invocation picks up the next task
1. **Error Handling** - Failed tasks cascade failures to all dependents

## Planned Future Enhancements

- **Task Prioritization** - Allow high-priority tasks to execute before others
- **Parallel Execution** - Execute independent tasks concurrently
- **Task Cancellation** - Allow canceling pending or in-progress tasks
- **Conditional Tasks** - Execute tasks based on conditions or previous results
