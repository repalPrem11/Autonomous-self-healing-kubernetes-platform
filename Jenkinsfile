pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        ACCOUNT_ID = '524178179120'
        ECR_REPOSITORY = 'payment-service'
    }

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
	stage('Build Docker Image') {
    	     steps {
        	dir('payment-service') {
            	   sh '''
                       docker build \
                       -t payment-service:${BUILD_NUMBER} .
            '''
        	}
    	   }
	}
	 stage('Login to Amazon ECR') {
    steps {
        sh '''
            aws ecr get-login-password --region ${AWS_REGION} | \
            docker login \
            --username AWS \
            --password-stdin ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
        '''
    }
}
	 stage('Tag Docker Image') {
    steps {
        sh '''
            docker tag payment-service:${BUILD_NUMBER} \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}:${BUILD_NUMBER}
        '''

        sh 'docker images'
    }
}
	 stage('Push Docker Image') {
    steps {
        sh '''
            docker push \
            ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}:${BUILD_NUMBER}
        '''
    }
}
         stage('Update Kubernetes Manifest') {
    steps {
        sh '''
            sed -i "s|image: .*|image: ${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}:${BUILD_NUMBER}|" k8s/deployment.yaml

            echo "Updated deployment.yaml:"
            grep image k8s/deployment.yaml
        '''
    }
}
stage('Commit and Push Manifest') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'git-token',
            usernameVariable: 'GIT_USERNAME',
            passwordVariable: 'GIT_TOKEN'
        )]) {
            sh '''
                git config user.name "Jenkins"
                git config user.email "jenkins@example.com"

                git remote set-url origin https://${GIT_USERNAME}:${GIT_TOKEN}@github.com/repalPrem11/Autonomous-self-healing-kubernetes-platform.git

                git fetch origin

                git checkout -B main origin/main

                git add k8s/deployment.yaml

                git commit -m "Update image to ${BUILD_NUMBER}" || echo "Nothing to commit"

                git push origin HEAD:main
            '''
        }
    }
}
}
}
