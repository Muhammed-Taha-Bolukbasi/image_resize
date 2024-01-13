pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('app') {
      steps {
        sh 'python3 url.py'
      }
    }
  }
}
