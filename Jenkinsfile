pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checked out successfully.'
            }
        }

        stage('Verify Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'ls -R'
            }
        }
	stage('Verify Docker Context') {
    	     steps {
        	sh 'pwd'
        	sh 'ls -la'
        	sh 'ls -la payment-service'
    	     }
        }
    }
}
