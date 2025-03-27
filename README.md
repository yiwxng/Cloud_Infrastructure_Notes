# Cloud_Infrastructure_Notes
This is a repo that contains all my notes of AWS cloud resources and infrastructure from my internship during fall 2024 to winter 2025. 

Any information below does not represent the opinion of the company that I worked for, it also does not contain any confidential information of the team + company that I was in.

Background:
I was pretty clueless when I first joined my role here as a AWS dev ops engineering intern. I have not used AWS before nor did I have much knowledge of infrastructure code.


## Platform engineering 
what is a platform - the infra on which sw is executed, consisting hardware, cloud computing tools, os, and coordinating apps ( like differ os, hardwards - video editing 
- A good solutions architect looks at the existing environment and analyzes what technologies are available and what software product must be developed to provide the best solution for the problem that needs to be solved
- platform eng - building and maintaining the underlying platform that supports different applications/solutions 
- rls - Solution architects leverage the capabilities provided by platform engineers to create effective business solutions, while platform engineers evolve the platform based on the needs identified by solution architects.

understand what the customer wants/needs, make sure the infra resources we provide makes sense in the long run, secure, reliable, scalable, monitor, mainteinance.

### Designing a platform 
- means thinking long-term and big-picture. 
- creating an ecosystem that enables others to build and innovate more efficiently, rather than solving a single, specific problem. 
- goal is to provide a robust, flexible foundation that accelerates development, improves consistency, and reduces redundant work across an organization.

[todo: read this about infra architecture](https://www.architecturemaker.com/what-is-infrastructure-architecture/)

## architectural thinking / system thinking 
1. Understanding the technical details (the "how") of implementing infrastructure solutions.
2. Grasping the strategic reasons (the "why") behind architectural decisions.
3. Seeing how individual components fit into the larger ecosystem.
4. Considering long-term implications of infrastructure choices.
5. Aligning technical decisions with business goals and strategies.


## TOOLS:
- SFTP
- Kubernetes
- Dockers
- Gitlab
- AWS
  - AWS CLI 
- Terraform


## NETWORK from [Cisco Network Basics](https://www.netacad.com/launch?id=f393c38f-b410-4d2b-8275-70e144273519&tab=curriculum&view=b287f8a2-5740-52f7-b4ac-e1ef04a8770d)
network - connection of at least two 2 computer (wire/wireless) servers, mainframes to exchange info, resource and services. 
internet - inter connected networks 
network data 

network transmission speed and capacity 


## CONTAINERS - Kubernetes, EKS, Dockers

### Clusters

### Nodes 
- physical or vm that provide computing resources for the cluster
- can host many pods 

### Pods (logical application units) 
- pods run on nodes, and scheduled to a specific node by k8s scheduler 
- pod is the smallest unit in Kubernetes, pods can contain containers, attach pcv 
- pods dont have direct access to pv, they have to mount the storage as a directory in the pod, it is an abstraction 
- container will use the directory, but it is really the pv storing the data
- pod will only the pvc name not the pv

### Containers 
- packaged application code and its dependencies 


### Volume 
- 2 types: non-persisting, persisting 
- non-persisting : empDir  - mostly used for container to share temp data 
- persisting : PV (persisting volume) - indepedent of pod but can be attached to a pod 
  - pv claim : the request from a pod (they only exist in pods level), the thing that connects pods and pv,  containers in same pod will use same pvc 


### Container, pods, volume 
- application will run in a container
- container do not persist data, when it is restarted it will lose all the data 
- volume is a storage element that will data in the container 

### Kubernetes vs. Laptop Analogy:
- Cluster = The entire laptop (the complete system)
- Node = The physical hardware (CPU, memory, disk)
- Operating System = Kubernetes itself (the management layer)
- Pod = An application process with its environment
- Container = The actual executable program and its dependencies

### Relationship btw: Terraform, AWS, Kubernetes, Dockers
(needs checking) 
- dockers: used for creating and running container for applications
- kubernetes : manages containerized application

## CI 

## CD 
te

## CICD Pipeline
an automated (can be different level) process that has many sequential stages, where each stage will use certain tools and data in order to stream line swd, testing, deployment  
where each stage of the pipeline is properly set up ahead of time for handoff consistent workflow -- the true automation in CICD

### stages of pipeline and the tools they will use:
1. Continuous Integration (CI):

Trigger: When code is pushed, this initiates the CI process.
Initialization: The CI system starts up based on the configuration.
Job Execution:

The 'build' job (compiling code or initializing Terraform)
The 'test' job (running unit tests or Terraform plan)


State Transitions: As these CI jobs complete, the pipeline state updates.
Conditional Flows: Decisions made based on CI results (e.g., stopping if tests fail).
Feedback Loop: Providing immediate feedback on build and test results.

Continuous Delivery/Deployment (CD):
3. Job Execution (continued):

The 'deploy' job (applying Terraform changes)


State Transitions: Updating pipeline state after deployment.
Conditional Flows: Decisions about proceeding to deployment based on previous steps.
Feedback Loop: Providing feedback on deployment results.
Completion: The entire process, including deployment, concludes.

### very simple ex
cloud infra resources, config of cicd,  runner to run the cicd config,

### what would the manual version of it look like?

## Terraform 
The tool and language that allows you to define, manage, reuse and destroy cloud infra resources.

terraform code - builds cloud infra resources 
terraform state - the information that keep track of the resources created/ what terraform knows about the current resource status

Terraform work stages:
1. write code for desired cloud infra
2. terraform generates a plan of all the resources that needs to be created, modified and deleted base on your code
  3.   the plan understand the order of resource creation. it uses dependecy graphs, the output of plan is the ordering the resources will be created.  
4. apply - the plan to create the resources. 

### yml file 
the cicd config that contains the terraform stages, testing....


### terraform stages and CICD relationship
Terraform provides the what of the infra, and cicd provides the how and the wehn 



### what if you want the resources to be created in a specific order?



I've learned a lot in my intern role, I believe one can summarize the main areas of cloud infrastructure into the six areas.




## what is devOps 




## what is cloud infrastructure?

### why do we/ companies use cloud infra now? and using less on prem?

### how do we build, use, maintain, destroy cloud infrastructure resouces?

## What are the six main areas of cloud infrastructure? With specific examples from AWS.
1. Core infrastructure
2. security and governance
3. data and application management
4. monitoring and optimization
5. specialized areas
6. automation.

| **Cloud Infrastructure Area**   | **Topic**                     | **Key Tasks**   | **AWS Correspondence**   |
|---------------------------------|-------------------------------|-----------------|--------------------------|
| Core Infrastructure             | Compute                      |                 |                          |
|                                 | Storage                      |                 |                          |
|                                 | Networking                   |                 |                          |
| Security and Governance         | security                     |                 |                          |
|                                 | governance and compliance    |                 |                          |
| Data and Application Management | data management              |                 |                          |
|                                 | application deployment       |                 |                          |
|                                 | AI/ML                        |                 |                          |
| Monitoring and Optimization     | Monitoring and Observability |                 |                          |
|                                 | cost optimization            |                 |                          |
| Specialized Areas               | edge and content delivery    |                 |                          |
|                                 | Hybrid and Multi-cloud       |                 |                          |
|                                 | IoT                          |                 |                          |
| Automation                      | automation                   |                 |                          |


Services I used:
- DMS
- IAM
- RDS
- CloudWatch
- CloudTrail
- S3
- Secret Manager


## CloudTrail
a service that does account-wise recording users  of api calls, user activities, time of action
for auditing event, security monitoring, operational troubleshooting 

types of event you can record 
1. management event - control plane action (creation/deletion resources)
2. Data event - high volume data plane actions (read/write to resources)
3. CloudTrail event - unususal write api calls 

How ?
- cloudtrail can send logs to both cloudwatch and s3, where s3 cna have strict permission and is necessary as the event source


Elements of CT
- event history (90 days)
- events (3 types)
- Trails (delivers event to s3)
- data lake (stores events recorded by CT, store for 7 years)
- CT insights for unusual patterns


## IAM 


IAM - Role
- assume role - when the original account role allows a different account to temporary use the role's permission for a resources, if not specified, can not assume role
- creation of role and attach it to group, roles
  - users get assigned to groups 

### iam resources : cloud and on-prem 

#### on-prem
- require access keys (why? because it is an external resource)


### IAM Users and Roles
User - use when you need to grant long-term access, require access keys, actual user access to aws console - actual users, on-prem, services outside of aws(api) that needs its resources would need users
Roles - temp security credentials for accessing aws resources, cross account access, allowing other aws services to have access to another service (example ec2 can assume role to access s3, without needing a user), federated identity ( allowing authenticated users across different systems) 

### Using users and roles togather ?
example: multi-environment s3 access for certain tools 
- create users for long term credentials, used for certain tools to authenticate with aws
- roles : different roles with different level of access/ s3 buckets
- rls : grant users permission to assume the roles
- why : seperation of concerns - user handle authentication, role manages authorization,
- can adjust one, without changing much of the other one, iam user doesnt have direct access to s3
