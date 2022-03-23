# Plan-A-DevOps-challenge-level-1--solution
## USAGE
This solution deploys a simple flask service to return information as a json response.
### STEP 1
To run this application, you will need to deploy a simple cluster using minikube or any k8s offering of your choice.
### STEP 2
After is fully up and running, configure kubectl to comunicate with cluster.
### STEP 3
cd in the "deployment" directory to get access to deployment files
### STEP 4
run the 'kubectl apply -f devops-deployment.yaml' to deploy infrastructure.