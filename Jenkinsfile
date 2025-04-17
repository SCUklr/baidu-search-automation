pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8'
        BROWSER = 'chrome'
        HEADLESS = 'true'
    }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    try {
                        bat 'pytest tests/ --alluredir=allure-results -v --capture=no'
                        currentBuild.result = 'SUCCESS'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("测试执行失败: ${e.message}")
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                // 如果测试全部通过，强制设置构建状态为SUCCESS
                if (currentBuild.result == 'SUCCESS' || currentBuild.result == null) {
                    currentBuild.result = 'SUCCESS'
                }
                
                allure([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
        success {
            echo '所有测试用例执行成功！'
        }
        failure {
            echo '测试执行失败，请检查日志！'
        }
    }
} 