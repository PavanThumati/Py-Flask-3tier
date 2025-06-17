first create database(RDS) and aws eks cluster in the same vpc
In RDS database security add the inbound rule for MYSQL with SOURCE of security group og the worker nodes
And create the deployment and service for app tier you will get a load balancer ID 

Add that app tier load balaner in the web/nginx.conf file and create the image for the web tier and then 

create teh deployment & service for web tier and then you can access the load balancer in the external world
