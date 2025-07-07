pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clone code') {
            steps {
                git 'https://github.com/LiLyTampone/Python-app.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    echo "Ứng dụng đã sẵn sàng để deploy"
                    # Ví dụ: scp hoặc ssh để deploy lên server nếu cần
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline kết thúc.'
        }
    }
}
