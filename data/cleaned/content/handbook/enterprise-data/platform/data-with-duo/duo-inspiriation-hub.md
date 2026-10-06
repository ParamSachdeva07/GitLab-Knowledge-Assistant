---
title: "Duo Inspiration Hub"
description: "Ideas for Duo: Prompts and Strategies"
---

### Description

Welcome to the Collaborative Ideas Hub, a dynamic workspace where data professionals can share, learn, and innovate together. This page invites users to explore a wealth of ideas and practices related to data analysis, automation, and compliance. By contributing your own insights and experiences, you can help build a vibrant community dedicated to enhancing our collective understanding and effectiveness in data-driven environments.

### Introduction

In the rapidly evolving field of data analytics, collaboration and knowledge sharing are essential for fostering innovation and continuous improvement. The Collaborative Ideas Hub serves as a central gathering space where data enthusiasts can exchange ideas, showcase their projects, and learn from one another's experiences.

This hub has been updated with the latest GitLab Duo capabilities including the **Duo Planner Agent** (Beta) and **Duo Security Analyst Agent** (Beta) introduced in GitLab 18.5, along with proven prompts from engineering teams across GitLab.

### 1. **Data Analysis Assistance**

* **Exploratory Data Analysis (EDA):** Duo can guide users on how to conduct EDA, suggest Python or SQL code snippets, or explain results from statistical models and visualizations.
  * **Prompt:** "I have a dataset with columns for age, income, and purchase history. Can you suggest Python code to perform exploratory data analysis, including visualizations and summary statistics?"
* **SQL Query Generation:** Snowflake Copilot or Duo can help write complex SQL queries, optimize them for better performance, and provide explanations for different query structures.
  * **Prompt:** "Write a SQL query to calculate the average order value for customers who have made more than three purchases in the last six months."
* **Statistical Analysis:** Assist in explaining or performing statistical techniques like hypothesis testing, regression analysis, and correlation calculations.
  * **Prompt:** "Can you explain how to run a linear regression in Python to predict housing prices based on square footage and number of bedrooms?"

### 2. **Automating Data Documentation**

* **Code Explanation:** It can generate detailed explanations or summaries of scripts or functions in Python, R, or SQL.
  * **Prompt:** "Can you explain this Python function that calculates the moving average of stock prices in simple terms?"
* **Project Documentation:** Automate the creation of project documentation by summarizing workflows, codebases, or data pipeline processes.
  * **Prompt:** "Generate a summary of this data pipeline that pulls data from Snowflake, transforms it in Python, and then uploads the results to a Tableau dashboard."
* **Glossary Creation:** Automatically generate glossaries for key terms, functions, or dataset variables used in data projects.
  * **Prompt:** "Create a glossary for a data project that includes terms like ETL, data warehouse, normalization, and machine learning."

### 3. **Code Troubleshooting and Optimization**

* **Debugging:** Help diagnose issues with Python, R, or SQL code, suggest solutions, and fix common errors in data workflows.
  * **Prompt:** "I’m getting an error when trying to merge two pandas DataFrames on a date column. Here's my code. Can you help me identify what’s wrong?"
* **Refactoring Code:** Provide recommendations for optimizing and refactoring code to improve readability and performance.
  * **Prompt:** "Here’s my Python code that calculates statistics for a dataset. Can you suggest improvements for readability and performance?"

### 4. **Workflow and Process Optimization**

* **Pipeline Monitoring:** Analyze logs and provide insights about data pipeline failures, delays, or anomalies.
  * **Prompt:** "Analyze this error log from our data pipeline and suggest possible causes for why the ETL process failed midway through the transformation step."
* **Procedure Automation:** Assist in automating parts of workflows by generating scripts to run common processes like ETL tasks or data validation.
  * **Prompt:** "Generate a Python script to automate the process of checking for missing data in a CSV file and logging the results."
* **Guiding Best Practices:** Find recommendations for improving your data governance, code reviews, and documentation processes.
  * **Prompt:** "What are some best practices for managing and documenting version control in a data science project?"

### 5. **Supporting Tableau or BI Dashboards and Reporting**

* **Analysis**
  * **Create a calculated fields**
    * **Prompt:** "Can you help me create a calculated field to display a rolling 12-month average of sales data in Tableau?" This can help with window functions, Level of Detail (LOD), Date formatting, etc.
  * **Create a Custom SQL Query**
    * **Prompt:** "Help me write a query to retrieve data from Snowflake and filter the results by the last 30 days before feeding it into a Tableau dashboard."
  * **Help teams identify relevant KPIs and metrics**
    * **Prompt:** "Suggest key performance indicators (KPIs) for a retail dashboard focused on customer retention and sales growth."
* **Report Summarization:** Summarize data insights or the results of analyses into concise and clear language for stakeholders.
  * **Prompt:** "Summarize the key findings from this dataset, including total sales by region, customer churn rate, and the top-selling product."
* **Documentation**
  * **Write a dashboard description**
    * **Prompt:** "I have a dashboard reporting on Customer Success achieving attainment goals, write a 2 sentence description for the dashboard."
  * **Write metrics definitions**
    * **Prompt:** "Write a one sentence definition for these 5 metrics: (Include list)."
* **Performance and Issues**
  * **Load Performance**
    * **Prompt:** "What are some common reasons for a Tableau workbook to load slowly, and how can I troubleshoot the performance issues?"

### 6. **Natural Language Queries on Data**

* **Conversational Analytics:** Enable non-technical users to ask questions about the data in natural language and receive relevant results or insights without needing to write SQL or code.
  * **Prompt:** "What are the total sales for Q2 this year, and how do they compare with Q1, based on this dataset?"
* **Data Summary Generation:** Generate summaries of datasets, highlighting outliers, key trends, or summary statistics automatically.
  * **Prompt:** "Summarize this dataset by providing key statistics like mean, median, standard deviation, and any noticeable trends or outliers."

### 7. **Enhancing Data Security and Compliance**

* **Compliance Queries:** Provide quick answers or reminders about data governance, privacy laws (like GDPR), or security protocols your team needs to follow.
  * **Prompt:** "What are the key data privacy regulations we need to follow when storing customer data in Europe?"
* **Policy Creation:** Assist in writing or refining data security and compliance policies tailored to your organization's needs.
  * **Prompt:** "Help us draft a data security policy for our organization, focusing on access control, encryption, and secure backups."

### **8. Other Analysis Use Cases**

* **Regular Expressions (Regex)**
  * **Prompt:** "Help me write a regex pattern to match email addresses, ensuring it captures both the local part and the domain correctly."
* **Cron Job Scheduling**
  * **Prompt:** "How do I write a cron job that runs a Python script every day at 3 AM?"
* **Data Cleaning Scripts**
  * **Prompt:** "Can you provide a Python script that removes duplicates from a CSV file and saves the cleaned data to a new file?"
* **API Request Formatting**
  * **Prompt:** "Help me format an API request in Python using the requests library to fetch data from a public REST API."
* **Automating Data Backups**
  * **Prompt:** "Can you suggest a Bash script to back up a directory to an external drive every Sunday at midnight?"
* **Unit Testing Code**
  * **Prompt:** "How do I write a unit test in Python for a function that calculates the factorial of a number?"
* **JSON Data Manipulation**
  * **Prompt:** "Write a Python function to parse a JSON file and extract specific fields into a Pandas DataFrame."
* **Git Commands and Workflows**
  * **Prompt:** "What are the Git commands to create a new branch, switch to it, and push it to the remote repository?"
* **Database Query Optimization**
  * **Prompt:** "How can I optimize a SQL query that selects records from a large table while ensuring it runs efficiently?"
* **Environment Variable Management**
  * **Prompt:** "How do I set environment variables in a .env file for a Python application using the dotenv package?"

### **9. GitLab Duo Planner Agent (Beta)**

GitLab Duo Planner is a specialized AI agent introduced in GitLab 18.5 that assists with product management and planning workflows. According to the [official documentation](https://docs.gitlab.com/user/duo_agent_platform/agents/foundational_agents/planner/), it helps with prioritization, work breakdown, dependency analysis, planning sessions, status reporting, backlog management, and estimation.

Below are the example prompts from the GitLab Duo Planner documentation:

* **Prioritization**
  * **Prompt:** "Help me prioritize issues in my backlog with the label (insert label name)" using the RICE framework."
  * **Prompt:** "Use MoSCoW to categorize features with the criteria (insert criteria) based on customer impact."
  * **Prompt:** "Which of the bugs with a "boards" label should we fix first, considering user impact?"
  * **Prompt:** "Rank these epics by strategic value for Q1."
  * **Prompt:** "Help me prioritize technical debt against new features."
  * **Prompt:** "Compare these features (insert URLs) using an effort versus impact matrix."

* **Work Breakdown and Scoping**
  * **Prompt:** "Which child items on this epic should I remove from the current scope to meet the deadline?"
  * **Prompt:** "Break down this initiative (insert URL) into key features we need to deliver."
  * **Prompt:** "Create user stories for this epic (insert URL) with acceptance criteria."
  * **Prompt:** "What tasks are needed to implement this user story?"
  * **Prompt:** "Suggest a phased approach for this project: (insert URL)"
  * **Prompt:** "What would be the MVP version of this feature? (insert URL)"
  * **Prompt:** "Identify which features are required for version 1, and which are optional, and explain why: (insert URL)"

* **Planning and Organization**
  * **Prompt:** "Suggest how to organize these 20 issues (insert filter criteria) across Q1 sprints."
  * **Prompt:** "What work should we defer in this epic (insert URL) to reduce scope?"
  * **Prompt:** "Review this backlog (insert filter criteria) and identify items that need refinement."
  * **Prompt:** "How should we sequence the features in this initiative? (insert URL)?"
  * **Prompt:** "Group these issues into logical release themes: (insert URL)"

* **Status Reporting and Communication**
  * **Prompt:** "Generate an executive summary of this epic's progress: (insert URL)"
  * **Prompt:** "Draft release notes based on issues assigned to (insert relevant milestone or iteration)."
  * **Prompt:** "Write a stakeholder update on this initiative's health: (insert URL)"
  * **Prompt:** "Summarize blockers and mitigation plans for leadership: (insert URL)"

* **Backlog Management**
  * **Prompt:** "Find stale issues that haven't been updated in 6 months."
  * **Prompt:** "Identify duplicate or similar issues in this project."
  * **Prompt:** "Which issues are missing estimates or assignees?"
  * **Prompt:** "Identify orphaned issues with no parent."
  * **Prompt:** "What issues have missed their due dates?"

### **10. GitLab Duo Security Analyst Agent (Beta)**

The GitLab Duo Security Analyst Agent, available in the AI Catalog as of GitLab 18.5, automates security workflows and vulnerability management through natural language commands in GitLab Duo Agentic Chat. According to the [GitLab 18.5 release](https://about.gitlab.com/releases/2025/10/16/gitlab-18-5-released/), the agent performs the following tasks:

* **List and View Vulnerabilities**
  * **Prompt:** "List all vulnerabilities in the current project."
  * **Prompt:** "Get detailed information for vulnerability [vulnerability ID], including CVE data and EPSS scores."
  * **Prompt:** "List all vulnerabilities in [project name] with detailed information including CVE data and EPSS scores for each vulnerability."

* **Manage Vulnerability Status**
  * **Prompt:** "Confirm and dismiss the following low-severity vulnerabilities that have been assessed and determined to be false positives: [list vulnerability IDs]."
  * **Prompt:** "Update the severity level of vulnerability CVE-2024-XXXX to 'High' based on recent threat intelligence."
  * **Prompt:** "Revert the status of vulnerability [vulnerability ID] back to 'detected'."

* **Create and Link Vulnerability Issues**
  * **Prompt:** "Create a vulnerability issue for CVE-2024-XXXX with detailed information and remediation recommendations."
  * **Prompt:** "Create vulnerability issues for all Critical and High severity vulnerabilities found in the last security scan."
  * **Prompt:** "Link vulnerability [vulnerability ID] to existing issue [issue URL or number]."
  * **Prompt:** "Link existing vulnerability issues to their corresponding merge requests and track remediation progress."

### **11. Engineering and Development Workflows**

* **Retrospective Analysis**
  * **Prompt:** "You are an engineering manager with experience in team retrospectives and continuous improvement. Please analyze the following retrospective issue comments and provide a comprehensive summary. Focus on: 1) Key Discussion Points - Extract the main themes, concerns, and topics discussed by team members, 2) What Went Well - Identify positive outcomes, successful practices, and achievements mentioned, 3) Areas for Improvement - Highlight challenges, pain points, and areas that need attention, 4) Action Items - Suggest specific, actionable next steps based on the discussion, 5) Team Sentiment - Assess the overall tone and morale of the team. Format the response with sections for Summary, Discussion Themes, Challenges, and Recommended Actions."
* **Issue Refinement and Planning**
  * **Prompt:** "You are an experienced software engineer with expertise in GitLab development, CI/CD pipelines, and software supply chain security. Please analyze the following issue description and create a detailed implementation plan. Provide: 1) Why are we doing this work - Clear articulation of the problem being solved, 2) Non-functional requirements - Documentation, feature flags, performance, testing, security, backward compatibility, 3) Implementation Plan - Step-by-step technical approach with dependencies, code changes, database changes, components involved, 4) Verification Steps - How to test and verify in different environments, 5) Risk Assessment - Potential challenges and mitigation strategies, 6) Estimated Complexity - Suggest a weight based on scope and complexity."
* **Code Review Best Practices**
  * **Prompt:** "Review this merge request for potential issues related to security, performance, maintainability, and best practices. Provide specific suggestions for improvement."
* **Technical Documentation**
  * **Prompt:** "Generate comprehensive technical documentation for this feature, including architecture overview, API endpoints, usage examples, and troubleshooting guide."

### **12. GitLab Duo Chat and Code Generation**

GitLab Duo Chat provides an interactive AI assistant that can help with code generation, explanations, refactoring, and more directly within your IDE or GitLab interface.

* **Code Explanation**
  * **Prompt:** "Explain what this code does in simple terms, including any potential edge cases or performance considerations."
* **Code Generation**
  * **Prompt:** "Generate a Python function that validates email addresses using regex and returns True if valid, False otherwise, with proper error handling."
* **Code Refactoring**
  * **Prompt:** "Refactor this code to improve readability, reduce complexity, and follow best practices. Suggest design patterns where appropriate."
* **Test Generation**
  * **Prompt:** "Generate comprehensive unit tests for this function, including edge cases, error conditions, and normal use cases."
* **Bug Identification**
  * **Prompt:** "Analyze this code for potential bugs, security vulnerabilities, or logical errors. Provide explanations and suggested fixes."
* **Performance Optimization**
  * **Prompt:** "Review this code for performance issues and suggest optimizations, particularly around database queries, loops, and memory usage."
* **Migration Assistance**
  * **Prompt:** "Help me migrate this code from Python 2 to Python 3, identifying breaking changes and suggesting modern alternatives."
* **API Integration**
  * **Prompt:** "Show me how to integrate with the [API name] REST API, including authentication, error handling, and rate limiting."

### **13. Top Prompts from Team Usage**

Here are the most frequently used prompts by GitLab teams:

* **Test Generation**
  * **Prompt:** "Write tests for the code user selected inside `<selected_code></selected_code>` tags."
    * **Usage:** Automatically generate unit tests for selected code
    * **Best for:** Any function, class, or code block that needs test coverage
  * **Prompt:** "Generate comprehensive unit tests for this function, including edge cases and error conditions."
  * **Prompt:** "Create integration tests for [feature_name] that cover the main user workflows."
  * **Prompt:** "Write test cases for this API endpoint including success, failure, and validation scenarios."

* **Code Refactoring**
  * **Prompt:** "Refactor the code user selected inside `<selected_code></selected_code>` tags."
    * **Usage:** Improve code quality, readability, and maintainability
    * **Best for:** Legacy code, complex logic, or code that violates best practices
  * **Prompt:** "Refactor this code to follow [coding_standard] best practices and improve readability."
  * **Prompt:** "Simplify this complex function by breaking it into smaller, more focused functions."
  * **Prompt:** "Refactor this code to remove duplication and extract common patterns into reusable utilities."

* **Code Explanation**
  * **Prompt:** "Explain the code user selected inside `<selected_code></selected_code>` tags."
    * **Usage:** Understand unfamiliar or complex code
    * **Best for:** Onboarding, code reviews, or working with legacy systems
  * **Prompt:** "Explain what this code does in simple terms, including any edge cases or gotchas."
  * **Prompt:** "Walk me through this algorithm step-by-step and explain the time/space complexity."
  * **Prompt:** "Explain how this code fits into the larger system and what its dependencies are."

* **Code Review and Quality**
  * **Prompt:** "Review this code for potential bugs, security vulnerabilities, and performance issues."
  * **Prompt:** "Check this code against our coding standards and suggest improvements."
  * **Prompt:** "Identify any anti-patterns or code smells in this implementation."
  * **Prompt:** "Review this merge request for code quality and provide specific, actionable feedback."

* **Documentation Generation**
  * **Prompt:** "Generate documentation for this function/class including parameters, return values, and usage examples."
  * **Prompt:** "Create inline comments explaining the complex logic in this code block."
  * **Prompt:** "Write a README section explaining how to use this module."
  * **Prompt:** "Document the API endpoints in this file with request/response examples."

* **Bug Fixing and Debugging**
  * **Prompt:** "Analyze this error message and suggest possible fixes: [error_message]"
  * **Prompt:** "Debug this code - it's supposed to do [expected_behavior] but instead does [actual_behavior]."
  * **Prompt:** "Find the bug in this code and explain why it's happening."
  * **Prompt:** "This code throws [exception_name] - what's wrong and how do I fix it?"

* **Code Generation**
  * **Prompt:** "Generate a [language] function that does [specific_task] with proper error handling."
  * **Prompt:** "Create a class that implements [interface_name] with all required methods."
  * **Prompt:** "Write code to parse [data_format] and extract [specific_fields]."
  * **Prompt:** "Generate boilerplate code for a REST API endpoint that handles [operation]."

### **Contributing to This Hub**

We encourage all team members to contribute their own successful Duo prompts and use cases! If you've discovered effective prompts or innovative ways to use GitLab Duo in your work, please consider adding them to this page or sharing them with the Data Platform team.
