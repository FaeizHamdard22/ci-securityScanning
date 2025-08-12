# Flask Application with Docker and Trivy Security Scanning in Jenkins

## Overview

This project is a simple Flask application containerized with Docker.
It also integrates **Trivy** vulnerability scanning into a Jenkins pipeline to ensure the built Docker image is checked for security issues before deployment.

## Features

* Simple Flask API returning a greeting message.
* Dockerized for consistent environment setup.
* Jenkins Pipeline with Trivy vulnerability scanning.
* Scans for **CRITICAL** vulnerabilities before deployment.

## Project Structure

```
my-flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## Flask Application

The app simply returns:

```
Hello, my name is Faeiz
```

### `app.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is Faeiz"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Docker Setup

### Dockerfile

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### Build and Run Locally

```bash
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
```

Then open: [http://localhost:5000](http://localhost:5000)

## Jenkins Pipeline Integration

The Jenkinsfile includes:

1. Build Docker image.
2. Scan image with Trivy for CRITICAL vulnerabilities.
3. Fail build if vulnerabilities are found.

### Jenkinsfile (Example)

```groovy
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
        stage('Trivy Security Scan') {
            steps {
                sh '''
                    trivy --version
                    trivy image --timeout 5m --exit-code 1 \
                        --severity CRITICAL ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }
}
```

## Requirements

* Docker installed
* Jenkins installed and configured
* Trivy installed on Jenkins node

## Running the Pipeline

1. Push the code to your Git repository.
2. Configure a Jenkins job to pull this repository.
3. Run the pipeline — it will build the Docker image and scan for vulnerabilities.


If you want, I can **add a section that explains how to persist Trivy’s cache in Jenkins** so it doesn’t download the DB every time.
Do you want me to include that?
