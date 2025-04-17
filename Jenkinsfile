pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8'
        BROWSER = 'chrome'
        HEADLESS = 'true'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                script {
                    try {
                        bat 'python -V'
                    } catch (Exception e) {
                        error "Python not found. Please install Python and add it to PATH"
                    }
                    bat 'python -m pip install --upgrade pip'
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    try {
                        bat 'mkdir allure-results'
                    } catch (Exception e) {
                        echo "Directory may already exist"
                    }
                    bat 'python -m pytest tests/ --alluredir=allure-results'
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
    
    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
        }
    }
} 