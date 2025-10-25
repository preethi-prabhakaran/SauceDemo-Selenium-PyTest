pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t saucedemo-tests .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm -e BASE_URL="https://www.saucedemo.com/" -v $PWD/reports:/app/results saucedemo-tests'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Saucedemo Test Report'
                ])
            }
        }
    }
}
