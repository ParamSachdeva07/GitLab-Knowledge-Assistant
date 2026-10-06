---
title: Deploying a test instance of Keycloak
category: Infrastructure for troubleshooting
description: "Support Engineer test environment setup options and guidelines"
---

## Deploying a test instance of Keycloak

### Prerequisites

- Create a VM with an external IP address; RHEL8-based commands are used in this example.
- Make sure that ports 8080 and 8443 are accessible on this VM.
- Pick up a hostname you will use for the Keycloak instance, obtain the external IP of the VM and configure A record on your DNS server to associate the IP address and the hostname. See [DNS for test instances](test_env.md#dns-for-test-instances) for details.
- Generate a certificate via https://punchsalad.com/ssl-certificate-generator/, DNS challenge is the simplest way to verify it. Have certificate and private key saved locally.

### Installation

1. Install PostgreSQL:

   ```shell
   dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   dnf -qy module disable postgresql
   dnf install -y postgresql16-server
   sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
   sudo systemctl enable postgresql-16
   sudo systemctl start postgresql-16
   ```

1. Create the database & user for Keycloak:

   ```shell
   sudo -u postgres psql
   CREATE USER keycloak WITH PASSWORD 'your-database-password';
   CREATE DATABASE keycloak OWNER keycloak;
   GRANT ALL PRIVILEGES ON DATABASE keycloak TO keycloak;
   ```

1. Install java and keycloak:

   ```shell
   yum install java-21-openjdk-devel wget -y
   cd /opt
   sudo wget https://github.com/keycloak/keycloak/releases/download/26.0.7/keycloak-26.0.7.tar.gz
   sudo tar -xzf keycloak-26.0.7.tar.gz
   sudo mv keycloak-26.0.7 keycloak
   ```

1. Configure a simple instance to check if DB connectivity is fine by adding the below lines to `/opt/keycloak/conf/keycloak.conf`:

   ```shell
   db=postgres
   db-username=keycloak
   db-password=your-database-password
   hostname=your-host-name.domain.tld
   http-enabled=true
   http-port=8080
   ```

1. Start keycloak and open http://your-host-name.domain.tld:8080 in browser to check that it's working. UI will open, but it won't be usable without HTTPS:

   ```shell
   cd /opt/keycloak
   ./bin/kc.sh bootstrap-admin user --bootstrap-admin-username admin --bootstrap-admin-password keycloak-password
   ./bin/kc.sh start
   ```

1. Stop keycloak, then configure it with HTTPS by adding the following values to `/opt/keycloak/conf/keycloak.conf`, make sure to put the certificate and key in respective locations:

   ```shell
   https-port=8443
   https-certificate-file=/opt/keycloak/conf/certificate.pem
   https-certificate-key-file=/opt/keycloak/conf/key.pem
   ```

1. Start keycloak again: you should be able to login now via https://your-host-name.domain.tld:8443 using the credentials you've set via the command line.
