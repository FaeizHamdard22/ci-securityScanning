pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-flask-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Security Scan with Trivy') {
            steps {
                script {
                   
                    sh '''
                        echo "Downloading Trivy vulnerability DB..."
                        trivy image --timeout 5m --exit-code 1 my-flask-app:latest

                    '''

                    
                    sh '''
                        echo "Running Trivy scan..."
                        trivy image --timeout 5m --exit-code 1 --severity CRITICAL ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'echo "Pushing Docker image..."'
          
            }
        }
    }
}
