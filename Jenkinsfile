pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
        PYTHON = 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Clone code') {
            steps {
                git branch: 'main', url: 'https://github.com/LiLyTampone/Python-app.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                    "%PYTHON%" -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    %VENV_DIR%\\Scripts\\pip.exe install --upgrade pip
                    %VENV_DIR%\\Scripts\\pip.exe install -r requirements.txt
                """
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    %VENV_DIR%\\Scripts\\pytest.exe tests
                """
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Ứng dụng đã sẵn sàng để deploy'
            }
        }
    }

    post {
        always {
            echo ' Pipeline kết thúc.'
        }
    }
}
