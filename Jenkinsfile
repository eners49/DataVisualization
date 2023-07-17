pipeline {
    agent any

    stages {
        stage('Compile & Run') {
            steps {
                sh 'python3 program.py'
            }
        }
    }

    post {
        success {
            sh 'echo "The job was successful."'
        }
        failure {
            sh 'echo "The job failed."'
        }
    }
}