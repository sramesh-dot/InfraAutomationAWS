pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Unit Tests') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                    .venv/bin/python -m unittest discover -s tests -v
                '''
            }
        }

        stage('Terraform Format Check') {
            steps {
                sh '''
                    terraform fmt -check -recursive terraform
                '''
            }
        }

        stage('Terraform Validate') {
            steps {
                dir('terraform') {
                    sh '''
                        terraform init -backend=false -input=false
                        terraform validate
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Python tests and Terraform validation passed.'
        }
        failure {
            echo 'Pipeline failed. Review the stage logs.'
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
