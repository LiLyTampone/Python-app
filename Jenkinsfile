pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clone code') {
            steps {
                git branch: 'main', url: 'https://github.com/LiLyTampone/Python-app.git'
            }
        }

stage('Setup Python') {
    steps {
        bat '''
            C:\Users\DELL\AppData\Local\Programs\Python\Python313\python.exe -m venv %VENV_DIR%
            call %VENV_DIR%\\Scripts\\activate.bat
            pip install --upgrade pip
            pip install -r requirements.txt
        '''
    }
}

  stage('Run Unit Tests') {
    steps {
        bat '''
            call %VENV_DIR%\\Scripts\\activate.bat
            pytest tests/
        '''
    }
}

        stage('Deploy') {
            steps {
                bat '''
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
