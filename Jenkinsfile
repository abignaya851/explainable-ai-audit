pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling the latest code from GitHub...'
                git branch: 'main', url: 'https://github.com/abignaya851/explainable-ai-audit.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                echo 'Training the model...'
                bat 'python train.py'
            }
        }

        stage('Generate Explanations') {
            steps {
                echo 'Running Explainable AI analysis...'
                bat 'python explain.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
