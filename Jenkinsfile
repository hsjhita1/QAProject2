pipeline{
    agent any
    stages{
        stage("Make scripts executable"){
            steps{
                sh 'printenv | sort'
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
