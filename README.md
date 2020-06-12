# QAProject2
# Table of Contents
* [Project Brief](#projectbrief)
  * [Scope & Additional Requirements](#scopeadditional)
  * [Risk Assessment](#riskassessment)
  * [Constraints](#constraints)
* [Architecture](#architecture)
  * [Project Tracking](#projecttracking)
  * [CI Server](#ciserver)
  * [Configuration Management](#ansible)
  * [Cloud Server](#cloudserver)
  * [Database](#database)
* [Testing](#testing)
* [Deployment](#deployment)
* [Self Reflection](#selfreflection)
* [Resources](#resources)

## Project Brief <a name="projectbrief"></a>
The purpose of this project was to create a service-orientated architecture for an application. The application must be composed of at least 4 services which work together.

### Scope & Additional Requirements <a name="scopeadditional"></a>
In addition to the project brief, there are a set of requirements which the project will also have to meet. These requirements are as followed:
* An Asana board
  * Should also provide a record of any issues
* An application integrated into a version control system
  * Using the feature branch model
  * Built through a CI server
  * Deployed to a cloud based virtual machine
  * Must feature a webhook so changes are deployed straight away
* Must follow the service-orinetated architecture provided
* Must be deployed using containerisation and an orchestration tool
* Create an Ansible Playbook
  * Should provision the environment
  
### Risk Assessment <a name="riskassessment"></a>
For this project, there were several risks which had to be indentified before the main body of the project was undertaken. This risk assessment included security of the database and application, and potential costs which the project may incur.

[Link to Risk Assessment](https://github.com/hsjhita1/QAProject2/blob/master/Documentation/RiskAssessmentQAProject2.xlsx)

### Constraints <a name="constraints"></a>
Due to the limited time and training, there were constraints in the project which impacted the choice of technology and services used. The project could only use technologies discussed during the training.

## Architecture <a name="architecture"></a>
As previously mentioned, due to constraints on the project, the following tools where chosen prior to starting the project. The tools and services listed below will be discussed in further detail and how each service was used.

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Database: GCP MYSQL Instance

### Project Tracking <a name="projecttracking"></a>
Trello was used to track progress for the project. Trello provided a card based tracking system which allowed easy tracking of what tasks had to be started, which tasks were in progress and which tasks had been completed. Labels were used to manage cards and what each card had represented e.g. Orange labels were used to show items which were part of the minimum viable product. A good thing about Trello are the powerups available and with the ability to have GitHub as a powerup, it allows easy tracking of commits related to task. The Trello board can be accessed through the link below: 

[Link to Trello Board](https://trello.com/b/xw1xj2pQ/sfia-project-2)

### CI Server <a name="ciserver"></a>
Jenkins was used as the CI Server for this project. A pipeline was set up for the project which used a variety of build steps to deploy the app. The picture below shows the steps in which Jenkins took to deplot the app. Firstly, it pulled the latest version from GitHub down automatically with a webhook. After pulling the project, it would then make scripts which I had created executable. This is very important because these scripts contained crucial steps which needed to be undertaken for the project to run. Next, any variables were sourced. This include the URI for my GCP SQL Instance. The next step was it to run my Ansible script and then finally my Docker Swarm script. The Ansible script would configure my VMs to have a environment in which my application would be able to run. Once this was done, Docker Swarm would then deploy onto my VMs.

![alt text](https://github.com/hsjhita1/QAProject2/blob/master/Documentation/Jenkins.png "Jenkins Pipeline")

### Configuration Management <a name="ansible"></a>
To configure each VM to the state required to run and deploy the application, Ansible was used for this. Creating a playbook allowed me to run tasks on multiple VMs. These tasks included in installing Docker on each machine, initializing my Docker Swarm and connecting my worker nodes to the swarm. To be efficient with the installs, roles and an inventory file were created.

Roles allowed me to reuse tasks for different machines. For example, Docker has to be installed on all machine whether it was a manager or worker node. With the inventory file, I could specify groups for my machines. This came in use for my worker nodes, allowing me to run roles on multiple machines. In this case, a role was created for all worker nodes which allowed the worker nodes to join the swarm.

### Cloud Server <a name="cloudserver"></a>
For this project, GCP was the cloud server used. GCP allowed me to create several virtual machines which were used to help deploy the application. Not only was GCP used for virtual machines, but was also used for the DBMS.

### Database <a name="database"></a>
GCP was used to host a MySQL instance which would provide the database for this project. As the application would have to persist some kind of data, I decided the best scenario for me would be to use a tool I was comfortable with. While I could have used a MySQL image on Docker, given how I had already had a previous configuration set up and would only need to change a single IP address, this made using GCP an easy choice for me database.

In terms of the data I would be storing, I would be storing previous results of the game with the data being stored also being read onto the home page so users can see a global list of results. Below is an example of how data will be stored in the database.

| ID | Difficulty | Score | Result |
| :-----: | :-----: | :-----: | :-----: |
| 1 | Easy | 36 | Even |
| 2 | Hard | 56 | Triple |
| 3 | Medium | 23 | Bust |

Below is the ERD used for this project. A single table was used to store the results of the game.

![alt text](https://github.com/hsjhita1/QAProject2/blob/master/Documentation/ERD.png "Initial ERD")

## Testing <a name="testing"></a>
Testing was done via PyTest and was conducted on each service. I had tried to implement a TDD approach towards this project but was unable to do this at a consistent level. Also, due to the nature of the project being micro-services and having not covered testing on this during my training, I had to find another way to test the services that had made requests from other services. There was the option of mock testing  but I was unable to implement it. However, my next approach of testing service 4 solved this issue. By being able to pass through the variables through the method rather than defining them and calling them in the method, I was able to test my code as if service 1 had requested the data from service 2 and 3 and then passed it to service 4. By doing it this way, I managed to implement my testing.

![alt text](https://github.com/hsjhita1/QAProject2/blob/master/Documentation/Testing.png "Testing")

### Links to all the coverage reports
* [Service 1](https://github.com/hsjhita1/QAProject2/blob/master/Service1/test_results/test-at-Jun-06-on-20-18%EF%80%BA36.pdf)
* [Service 2](https://github.com/hsjhita1/QAProject2/blob/master/Service2/test_results/test-at-Jun-06-on-20-10%EF%80%BA50.pdf)
* [Service 3](https://github.com/hsjhita1/QAProject2/blob/master/Service3/test_results/test-at-Jun-06-on-20-10%EF%80%BA45.pdf)
* [Service 4](https://github.com/hsjhita1/QAProject2/blob/master/Service4/test_results/test-at-Jun-06-on-20-10:38.pdf)

## Deployment <a name="deployment"></a>
![alt text](https://github.com/hsjhita1/QAProject2/blob/master/Documentation/CI%20Pipeline.png "Pipeline")

Initially, the code was developed in Visual Studio Code using Python and Flask. This code was them pushed to a VCS, in this case GitHub, wehre it would be stored inside a repository. To keep track on was tasks and code were completed, a Trello board was used. Once a task had been completed on Trelo, the task was attached to the commit in which it related to. Once a new task was taken on, the repository was pulled to make sure the latest code was on hand and then the task would then be carried out.

While I was coding, a webhook would automatically pull the code from GitHub to the CI Server, Jenkins. Using custom shell scripts and a Jenkinsfile, Jenkins was able to build each the microservices and deploy the application. The application was deployed using Docker Swarm Stack which deployed the application on multiple nodes which is beneficial for redundancy and availability. Along with Jenkins pulling the code using the webhook, Docker was automatically building the image once new code was being pushed. If new code was just being pushed, Docker will build the new code under the 'latest' tag. If code was pushed with a new build number, Docker will create a new 'latest' image and another image with the new build number. For example, if a build was pushed with the tag 1.10, Docker would create a 'latest' image with this tag and also a '1.10' image.

## Self Reflection <a name="selfreflection"></a>
Upon self reflection, I believe the final build of the application had met the necessary criteria of which the project had to fufill. The main focus of the architecture was to creata an application which was to be composed of at least 4 services which I managed to do. I had also managed to meet the rest f the requirements such as using Ansible to provision each environment and deploying the application using containerisation and an orchestration tool.

While I can say the overall project was a sucess, there are a few things on which I would improve on if I were to do it again.
1. Implementing the game to the fullest version. 
 
   The project was based on a game called Razzle Dazzle. The actual game has a different scoring system in which every number gives points and the aim of the game is to get 10 points from a total of 3 rolls. The way this could be implemented is by using a for loop to simulate 3 rolls and using more logic to filter out indvidual scoring for each number. While possible, the logic could get long but will provide a more realistic version of the game. 

   Another implementation to the game I can add is a potential stat feature which displays a percentage breakdown of all the results. For example, a chart could out of 'x amount of games', 'n games' had a result of Even and so on.

2. Implement extra tables
 
   After developing the application, even though the database was functional, I could have added in 2 extra tables and given them relationships. The proposed solution for this can be seen below
   ![alt text](https://github.com/hsjhita1/QAProject2/blob/master/Documentation/Proposed%20ERD.png "Proposed ERD")

3. Implementing CSS or styling

   With the little experience I have had with CSS and Styling, I maybe could have implemented some to improve the basic appearance of the site.

4. Using and learning more features in the tools used

   During this project, I had learnt about the GitHub releases section and when I had used it, I realised I could version control my project to a further level. This was implemented on Docker Hub using the the image tags but not on GitHub to the same level.

## Resources <a name="resources"></a>
### Docker Images
* [Service 1](https://hub.docker.com/repository/docker/hsjhita1/service1)
* [Service 2](https://hub.docker.com/repository/docker/hsjhita1/service2)
* [Service 3](https://hub.docker.com/repository/docker/hsjhita1/service3)
* [Service 4](https://hub.docker.com/repository/docker/hsjhita1/service4)

### Documentation
* [Trello Board](https://trello.com/b/xw1xj2pQ/sfia-project-2) 