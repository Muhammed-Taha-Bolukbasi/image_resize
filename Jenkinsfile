pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('requirements') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('app') {
      steps {
        sh 'python3 url.py'
      }
    }
  }
}