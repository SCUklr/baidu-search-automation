pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8'
        BROWSER = 'chrome'
        HEADLESS = 'true'
        BUILD_STATUS = 'SUCCESS'  // 默认设置为SUCCESS
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
                        env.BUILD_STATUS = 'SUCCESS'
                    } catch (Exception e) {
                        env.BUILD_STATUS = 'FAILURE'
                        error("测试执行失败: ${e.message}")
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                // 在生成报告之前设置构建状态
                if (env.BUILD_STATUS == 'SUCCESS') {
                    currentBuild.result = 'SUCCESS'
                }
            }
            
            allure([
                includeProperties: false,
                jdk: '',
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
            
            script {
                // 在生成报告之后再次确认构建状态
                if (env.BUILD_STATUS == 'SUCCESS') {
                    currentBuild.result = 'SUCCESS'
                }
            }
        }
        success {
            echo '所有测试用例执行成功！'
        }
        failure {
            echo '测试执行失败，请检查日志！'
        }
        unstable {
            script {
                // 如果状态变为unstable，但测试是成功的，强制改回success
                if (env.BUILD_STATUS == 'SUCCESS') {
                    currentBuild.result = 'SUCCESS'
                }
            }
        }
    }
} 