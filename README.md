# QAProject2
# Table of Contents
* [Project Brief](#projectbrief)
  * [Scope & Additional Requirements](#scopeadditional)
  * [Risk Assessment](#riskassessment)
  * [Constraints](#constraints)
* [Architecture](#architecture)
  * [Project Tracking](#projecttracking)
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

### Cloud Server <a name="cloudserver"></a>
For this project, GCP was the cloud server used. GCP allowed me to create several virtual machines which were used to help deploy the application. Not only was GCP used for virtual machines, but was also used for the DBMS

### Database <a name="database"></a>
GCP was used to host a MySQL instance which would provide the database for this project. As the application would have to persist some kind of data, I decided the best scenario for me would be to use a tool I was comfortable with. While I could have used a MySQL image on Docker, given how I had already had a previous configuration set up and would only need to change a single IP address, this made using GCP an easy choice for me database.

In terms of the data I would be storing, I would be storing previous results of the game with the data being stored also being read onto the home page so users can see a global list of results.

## Testing <a name="testing"></a>


## Deployment <a name="deployment"></a>


## Self Reflection <a name="selfreflection"></a>

## Resources <a name="resources"></a>
### Docker Images
* [Service 1](https://hub.docker.com/repository/docker/hsjhita1/service1)
* [Service 2](https://hub.docker.com/repository/docker/hsjhita1/service2)
* [Service 3](https://hub.docker.com/repository/docker/hsjhita1/service3)
* [Service 4](https://hub.docker.com/repository/docker/hsjhita1/service4)

### Documentation
* [Trello Board](https://trello.com/b/xw1xj2pQ/sfia-project-2) 

### Other
* [Main Webpage](http://34.89.58.143:5000/)
* [Service 2](http://34.89.58.143:5001/)
* [Service 3](http://34.89.58.143:5002/)
* [Service 4](http://34.89.58.143:5003/)
