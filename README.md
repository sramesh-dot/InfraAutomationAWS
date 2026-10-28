AWS Infrastructure Automation with Python, Terraform & Jenkins

Automate AWS infrastructure reporting and validate infrastructure configurations using Python, Terraform, Git, GitHub, and Jenkins CI/CD.

Project Overview

This project demonstrates hands-on cloud engineering and DevOps practices by combining AWS resource management with Infrastructure as Code (IaC) and Continuous Integration (CI).

The solution uses Python and Boto3 to generate EC2 instance reports, Terraform to manage AWS infrastructure, and Jenkins to automate Python unit tests and Terraform validation.

Architecture

Developer
   |
   v
Git / GitHub Repository
   |
   v
Jenkins CI Pipeline
   |
   +----> Python Dependency Installation
   |
   +----> Python Unit Tests (unittest)
   |
   +----> Terraform Format Check
   |
   +----> Terraform Validation
   |
   v
Validated Project
   |
   v
AWS Infrastructure
(Managed separately using Terraform)

Technology Stack

Technology	Purpose
AWS EC2	Cloud computing and instance management
AWS IAM	Identity and access management
Python	AWS automation and reporting
Boto3	Python SDK for AWS
Terraform	Infrastructure as Code
Jenkins	CI pipeline automation
Git & GitHub	Version control and source code management
Linux	Development and CI environment
Python unittest	Automated unit testing

Key Features

1. AWS EC2 Reporting with Python

* Uses Boto3 to retrieve EC2 instance information.
* Filters instances using the project tag Project=aws-python-terraform-jenkins.
* Reports instance IDs and current states.
* Uses AWS credentials supplied through the configured AWS credential chain or an attached IAM role rather than hardcoding credentials.

2. Infrastructure as Code with Terraform

* Identifies the default VPC in the configured AWS region.
* Creates and manages a project-specific security group.
* Applies resource tags for project identification and environment management.
* Uses Terraform variables to configure the project name, AWS region, and environment.
* Defines security group egress rules without adding inbound access rules.

3. Automated Python Testing

* Uses Python’s built-in unittest framework.
* Uses mocking to test application behavior without requiring live AWS API calls for unit tests.
* Helps detect regressions before changes are accepted.

4. Jenkins Continuous Integration

The Jenkins pipeline includes the following stages:

1. Checkout source code from GitHub.
2. Create a Python virtual environment and install dependencies.
3. Execute Python unit tests.
4. Check Terraform formatting.
5. Initialize Terraform without configuring a remote backend.
6. Validate Terraform configuration.

Current pipeline scope: testing and validation only. It does not run terraform apply or deploy infrastructure automatically.

Repository Structure

InfraAutomationAWS/
├── ec2_report.py
├── tests/
│   └── test_ec2_report.py
├── terraform/
│   ├── versions.tf
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── dev.tfvars.example
│   └── .terraform.lock.hcl
├── requirements.txt
├── Jenkinsfile
├── .gitignore
└── README.md

Terraform state files and local environment-specific variable files should remain excluded from version control.

Prerequisites

Install or configure the following:

* An AWS account with appropriate permissions.
* Python and pip.
* Git.
* Terraform CLI.
* Java and Jenkins.
* An AWS credential configuration or IAM role with the required permissions.
* GitHub repository access for Jenkins.

Setup and Installation

1. Clone the repository

git clone https://github.com/sramesh-dot/InfraAutomationAWS.git
cd InfraAutomationAWS

For a private repository, authenticate with GitHub using an approved credential or token. Never place access tokens in the repository URL.

2. Create a Python virtual environment

Linux:

python3 -m venv .venv
source .venv/bin/activate

Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Install dependencies

python -m pip install -r requirements.txt

4. Run the Python report

python ec2_report.py

The script reports the EC2 instances matching the configured project tag in the default region ap-southeast-2.

5. Run unit tests

python -m unittest discover -s tests -v

The tests use mocks to verify application behavior without requiring actual EC2 operations.

Terraform Usage

Run Terraform commands from the terraform directory.

1. Configure variables

cp dev.tfvars.example dev.tfvars

On Windows PowerShell:

Copy-Item dev.tfvars.example dev.tfvars

Review the values in dev.tfvars before proceeding.

2. Initialize Terraform

terraform init

3. Format and validate

terraform fmt -check
terraform validate

4. Review the proposed infrastructure changes

terraform plan -var-file=dev.tfvars

5. Apply only when you intend to change AWS infrastructure

terraform apply -var-file=dev.tfvars

Review the plan and estimated costs before confirming the operation. Terraform may create, update, or delete resources depending on the configuration and state.

Important: The Jenkins pipeline does not execute the apply command. The commands above are for deliberate manual infrastructure management.

Jenkins CI Pipeline

Create a Pipeline job in Jenkins and configure it as follows:

* Definition: Pipeline script from SCM
* SCM: Git
* Repository URL: https://github.com/sramesh-dot/InfraAutomationAWS.git
* Branch: */main
* Script Path: Jenkinsfile
* Credentials: Select a Jenkins-managed GitHub credential with read access to this private repository.

Run the job using Build Now and inspect Console Output if a stage fails.

The pipeline requires Python, Git, and Terraform to be available in the Jenkins build environment. Python dependencies are installed into a workspace virtual environment.

AWS Security Best Practices

* Use an EC2 instance profile or another supported temporary credential mechanism when possible.
* Follow least-privilege IAM principles and grant only the API actions required for the project.
* Never commit AWS access keys, secret keys, GitHub tokens, .env files, or private keys.
* Keep Terraform state and backup files out of Git because state can contain sensitive infrastructure information.
* Restrict inbound network access to security groups and services.
* Review Terraform plans before applying changes.
* Monitor AWS billing and resource usage, especially when working with a Free Tier account.

Future Enhancements

Potential improvements include:

* Triggering Jenkins builds automatically using GitHub webhooks.
* Adding automated test reports and pipeline notifications.
* Adding Terraform plan review and approval stages.
* Integrating security scanning for Terraform configurations.
* Introducing controlled deployment stages with approval gates.
* Deploying a sample application to AWS using a separate, cost-conscious deployment workflow.

These enhancements should be added and verified as they are implemented.

Author

Ramesh S
