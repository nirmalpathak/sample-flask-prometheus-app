pipeline {
   agent any

  options {
    buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
  }

   stages {
    stage('Cloning Git') {
      steps {
        git branch: 'master',
        url: 'https://github.com/nirmalpathak/sample-flask-prometheus-app.git'
      }
    }
      stage('Docker Build') {
         steps {
            sh 'docker build -t nirmalpathak/sample-flask-prometheus-app .'
         }
      }
      stage('Docker Publish') {
         steps {
            withDockerRegistry([ credentialsId: "nirmalpathak-docker-hub", url: "" ]) {
            sh 'docker push nirmalpathak/sample-flask-prometheus-app'
         }
        } 
      }
      stage('Deploy') {
         steps {
	    sh 'sed "s/v0.0.1/v0.${BUILD_NUMBER}/" my-flask-app.yaml |microk8s.kubectl apply -f-'
         }
      }
        stage('Status') {
         steps {
            sh 'microk8s.kubectl wait --for=condition=available --timeout=60s deployment.apps/my-flask-app'
         }
      }
   }
}
