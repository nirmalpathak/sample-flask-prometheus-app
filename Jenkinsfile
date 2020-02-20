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
            sh 'microk8s.kubectl run --generator=run-pod/v1 my-flask-app --image=nirmalpathak/sample-flask-prometheus-app'
         }
      }
        stage('Status') {
         steps {
            sh 'sleep 30; microk8s.kubectl get pods'
         }
      }
   }
}
