# Plan-A-DevOps-challenge-level-1--solution
## USAGE
This solution deploys a simple flask service to return information as a json response.
### STEP 1
To run this application, you will need to deploy a simple cluster using minikube or any k8s offering of your choice.
- step by step guide in setting up a minikube is found [here](https://minikube.sigs.k8s.io/docs/start/)
### STEP 2
After is fully up and running, configure kubectl to comunicate with cluster.
- step by step guide in setting up kubectl is found [here](https://kubernetes.io/docs/tasks/tools/)
### STEP 3
clone git repository and change directory into the folder "deployment"
```bash
  git clone https://github.com/Joshua-Igoni/Plan-A-DevOps-challenge-level-1--solution
  cd Plan-A-DevOps-challenge-level-1--solution/deployment
```
### STEP 4
Run the following command to deploy the docker container and service.
```bash
  kubectl apply -f devops-deployment.yaml
```