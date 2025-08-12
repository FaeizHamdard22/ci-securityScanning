pipeline {
    agent any

    environment {
        IMAGE_NAME = "faeiz-flask-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Security Scan with Trivy') {
            steps {
                script {
                   
                    sh """
                    if ! command -v trivy > /dev/null; then
                        curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh
                        sudo mv trivy /usr/local/bin/
                    fi
                    """

                
                    sh "trivy image --exit-code 1 --severity CRITICAL ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}
