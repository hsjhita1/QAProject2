pipeline{
    agent any
    stages{
        stage("Source variables"){
            steps{
                sh 'source ~/.bashrc'
                sh 'cd /home/jenkins/.jenkins/workspace/qa-project-2'
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
