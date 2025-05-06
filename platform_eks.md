

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