# Stack resources in this cft 

VPC
Route Table
IG
IG attachment to the VPC
2 Public Subnets
ASG for Private Subnets
Scaling Policy for Public Subnets
Route Table for Public Subnets
Public Subnets association to the Route Table
Security group ( HTTP & SSH to open to 0.0.0.0/0 )
Launch Template with Bootstrap script to install & launch Apache -- user data config
ASG for Public Subnets
Scaling Policy for Public Subnet
4 Private Subnets
