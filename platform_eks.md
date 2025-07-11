

DESIGN CONSIDERATIONS CHECKLIST

1. Functionality
What does the CSI driver do?
Why is it needed (what problem does it solve)?
Which teams or applications need this capability?
Is it compatible with our EKS version?
2. Deployment Strategy
Will this driver run as a DaemonSet, Deployment, or other controller?
Should it run on every node, or only on nodes used by specific teams?
Can/should it be installed as part of our existing EKS Terraform module, or separately?
Does it require Helm, kubectl manifests, or another install method?
3. Security & Access Control
How will IRSA (IAM Roles for Service Accounts) be used to restrict access to team-specific S3 buckets?
How is cross-tenant access prevented?
What IAM policies are required for the CSI driver to work properly?
Do we need bucket policies or KMS key policies to further restrict access?
Are Kubernetes RBAC policies enforced per namespace?
4. Tenant Isolation
How is access scoped to individual teams?
(e.g., one IAM role per team? one service account per namespace?)
Will each team define their own PVCs and mount buckets?
Are we enforcing namespace boundaries and network policies?
5. Cost & Performance
What are the resource costs (CPU, memory) per node if deployed as a DaemonSet?
Can we limit deployment scope to reduce cost?
Will this add-on increase storage or network traffic, and do we monitor that?
6. Operational Ownership
Who is responsible for:
Maintaining the add-on?
Updating it?
Handling on-call issues?
Do we have alerts/monitoring/logs configured for the driver?
7. Packaging & Automation
Is this part of our Terraform codebase? If so:
How is it parameterized for multi-tenant usage?
Do we need to allow opt-in per team (e.g., via variable toggle)?
Can we template or reuse Helm values per tenant?
8. Documentation & Onboarding
How does a team use this?
What are the steps to mount a bucket?
What policies or roles do they need?
Do we provide templates or examples?


What I think and learn from my time as a cloud platform engineer.

We are the people that design maybe not maybe this might maybe this is different for different companies due to you know the different business and personnel structures. But as a cloud platform engineer, I believe that we not only need to know how to build These solutions given to us, but also question and understand why these solutions make sense for the specific usage.

So every time that we propose a new cloud service or infrastructure service, we should be able to say that we chose this service because it meets our business, technical, and operational needs better than the alternative – and here is why.

1. Business alignment
 - Does this service support a key business goal or problem, how does it support the business goal or problem. Let's say we want faster file processing times and why how will that improve our customers experience. And
 - Is this service align with the companies and the regulators compliance, for certain industries, there are different body governing bodies that have guidelines and obligations in place.

 - example : Data has to stay in Canada, or has to be a certain format because of XYZ.

[todo] Have to understand how the relevant regulations in Canada impact the way that infrastructure is structured in the company

2. Functionality fit
 - Does this particular service do what we need to do?
  - with little or how much config 
 - Can is this service a better alternative for what we have existing? And if so, better in what ways?
  - Simplicity (easy to maintain) -> reduce tech dect and support 
  - Reliability (how consistently will this service do it intended work overtime?) -> system up/down time
  - Fault-tolerant (the ability of a system to continue to operate when parts of it fails, and how it handles that) 
  - Security (does it in for better security practises?) -> decrease risk of data breach, increase access control 
  - Integration into existing set up (does how easy does it integrate with our existing set up or tooling?) -> Produce complicated set ups that require  more support
  - Performance/latency : (Is it faster or more scalable and does it maintain or give us higher loads?) -> Supports growth improve user experience
  - Accountability/logging (does it provide equal or better observability or monitoring?)
  - Cost (is it cheaper or does it save more engineering effort)
  - Future (does it support potential future needs better than the existing?) -> future proof 
  
3. Cost and capability
 This is the price model predictable under expected usage, 
 what is the worst case of cost?
 Can we scale it horizontally with increased data increase tenant

 4. Operational impact
 - Is this service easy to monitor patch and operate?
 - How does it impact the existing set up for CICD

 5. Integration and migration how well does it fit into our existing cloud infrastructure what are the things that need to be set up to fit into the cloud infrastructure, and what would the migration from the current system look like?

 6. Risk of the service
  - How mature is the service? Is it in pre-
  - Any fallback plan when the service fails if it fails

  Long-term questions
   - Will this still work if our traffic doubles, 
   our security policy tightens, 
   a new team needs to be on boarded by a certain deadline



# K8s and Linux rls 
```bash 
|  Linux Skill                     |  Why It's Useful in Kubernetes    |
| -------------------------------- | ----------------------------------- |
| **Processes & signals**          | Understand container lifecycle      |
| **Filesystems & mounting**       | Volume mounts & PVs                 |
| **Users & permissions**          | Pod security context, runAsUser     |
| **Networking (netns, iptables)** | Pod-to-pod networking, services     |
| **Systemd/service management**   | Managing kubelet, containerd, CRI   |
| **cgroups & namespaces**         | Core to how containers are isolated |
| **Syscalls & logs**              | Debugging and performance           |
```

# Enabling POSIX-Style S3 Access via Kubernetes CSI: My Work on Cloud-Native File System Integratio

The first problem that i faced was a knowledge gap between linux (os) and k8s. but not knowing that is the foundational problem. 
which made me feel like I was running in circles in the layer between my intro to system knowledge, and k8s eks addon. 



# From writing Python file with functions and classes and methods to understanding K8. S

My previous understanding when coming into this internship was that applications that we use are built with languages such as Python or Java or C, where we talk about how our application will respond to inputs and what outputs they should get.
However in my internship, my second task was to create a module which was a new pattern at the time for a new EKS add on.  I did not understand from what I learned and how it relates to what I'm doing for work.

But now I think but below is a explanation and below is a attempt of my understanding from that to Kubernetes
1. we first write our application using maybe object oriented programming language like Python
2. We run the file in Python like "python app.py" -> OS will load the Python interpreter, Python.exe 
3. the interpreter is a program itself so the OS create a process
4. The interpreter will read the code and translate it into bytecode Which is executed by PVM
5. If the interpreter isn't installed on the system the program won't run, which is why some apps would only work depending on the other person's environment
6. which is why container comes into place. A container is a light way package with all libraries Dependencies included That allows the app to run in any environment
7. Also if you want to allow your app to be used by more than 1. person at the same time then you would use the help of Kubernetes which will help you to run as many instances as your app as it is needed for your users


Container - A special process that runs in a sandbox environment isolation from operating system
It differs from regular process in that it has its isolated file system it sees its own processes as the only process in the system, It cannot access POST file unless mounted, and it cannot affect the host system without privilege. 
And the key thing that isolates allows for isolation is name spaces and C groups. The namespaces isolates what the process can see and the C groups limits what the process can use.


mounts 
Amount point is a folder where contents of external devices appear, it is a path where another file system becomes accessible.
On the container the mount point will introduce a new system as a new path in the existing containers file system


# side note
When I am understanding when I am understanding and dictating these notes I realize that this process of understanding and this model of thinking about the world which is computational model is really what draws me into computer science more and more. in object oriented programming we learn to see the world and as objects with classes with its own methods its own relationship. And the core principles of abstraction encapsulation inheritance and interface.
And in I suppose system thinking, we view the world through scheduler, resources, file systems, users. 
It is this model of organizing logically separating and organizing information that allows me to see the world differently. In a more structured and a different logical way of thinking

