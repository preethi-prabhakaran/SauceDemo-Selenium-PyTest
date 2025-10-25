pipeline {
    agent any

    environment {
        IMAGE_NAME = "saucedemo-test"
        REPORT_DIR = "reports"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                bat 'docker run --rm -e BASE_URL="https://www.saucedemo.com/" -v %CD%/reports:/app/results %IMAGE_NAME%'
            }
        }

        stage('Publish Report') {
            steps {
                junit 'reports/junit_report.xml'
                publishHTML(target: [
                    allowMissing: false,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Saucedemo-Test-Report'
                ])
            }
        }
    }
}
