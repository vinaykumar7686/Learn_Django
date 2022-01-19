pipeline {
environment {
registry = "vinayk7686/testdeploy
registryCredential = 'vinayk7686'
dockerImage = 'testdeploy'
}
agent any
stages {
stage('Cloning our Git') {
steps {
git 'https://github.com/vinaykumar7686/Learn_Django.git'
}
}
stage('Building our image') {
steps{
script {
dockerImage = docker.build registry + ":$BUILD_NUMBER"
}
}
}
stage('Deploy our image') {
steps{
script {
docker.withRegistry( '', registryCredential ) {
dockerImage.push()
}
}
}
}
stage('Cleaning up') {
steps{
sh "docker rmi $registry:$BUILD_NUMBER"
}
}
}
}
