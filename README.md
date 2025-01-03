# Cloud_Infrastructure_Notes
This is a repo that contains all my notes of AWS cloud resources and infrastructure from my internship during fall 2024 to winter 2025. 

Any information below does not represent the opinion of the company that I worked for, it also does not contain any confidential information of the team + company that I was in.


I was pretty clueless when I first joined my role here as a AWS dev ops engineering intern. I have not used AWS before nor do I have much knowledge of infrastructure code.


## Terraform 
The tool and language that allows you to define, manage, reuse and destroy cloud infra resources.

terraform code - builds cloud infra resources 
terraform state - the information that keep track of the resources created/ what terraform knows about the current resource status

I've learned a lot in my intern role, I believe one can summarize the main areas of cloud infrastructure into the six areas.





## what is cloud infrastructure?

## why do we/ companies use cloud infra now? and using less on prem?

## how do we build, use, maintain, destroy cloud infrastructure resouces?

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


actions with iam:
- assume role - when the original account role allows a different account to temporary use the role's permission for a resources
- creation of role and attach it to group, roles
  - users get assigned to groups 


  
