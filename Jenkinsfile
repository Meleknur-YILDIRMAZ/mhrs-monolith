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

        stage('Cleanup Old Containers') {
            steps {
                bat 'docker rm -f mhrs_mongodb mhrs_rabbitmq mhrs_elasticsearch mhrs_backend mhrs_frontend 2>nul || exit /b 0'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker compose down --remove-orphans'
                bat 'docker compose up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Deploy basarili.'
        }
        failure {
            echo 'Pipeline basarisiz oldu.'
        }
    }
}