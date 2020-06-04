pipeline{
    agent any
    stages{
        stage("Source variables"){
            steps{
                sh 'source ~/.bashrc'
            }
        }
        stage("Make scripts executable"){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("Deploy Docker Swarm Stack"){
            steps{
                sh './script/docker.sh'
            }
        }
    }
}
