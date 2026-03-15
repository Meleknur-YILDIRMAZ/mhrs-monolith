pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                bat 'docker compose build backend'
            }
        }

        stage('Build Frontend') {
            steps {
                bat 'docker compose build frontend'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'echo Test stage'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker compose down'
                bat 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Deploy başarılı.'
        }
        failure {
            echo 'Pipeline başarısız oldu.'
        }
    }
}