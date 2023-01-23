#How to run deploy mongodb

step 1. First apply the command:
kubectl apply -f mongo-configmap.yaml
step 2.Then in the same way apply mongo-secret.yaml
step 3.Now its time to apply the mongodb-deployment.yaml in the same way.
step 4.When the database is deployed using the previous command ,it creates both the deployment and service in Kubernetes.
step 5.Now we can deploy our web application , for demo a web-client for mongo-db is added here which is mongo-express.yaml which should be replaced by the web-application of the project.Here is is used as a demo to check the database which offcourse could also be done from the terminal.
step 6.Check Ingress.Here mongo-express is used to configure ingress
step 7.Persistence Volume : The file pv-mongodb has configuration for Persistence Storage,the storage class is microk8s-hostpath which is mapped to local path in a VM : /opt/mongodb/data
First PV is created by allowcating a volume of type:hostPath and the the following PVC is applied.
step 8.Now pvc-mongodb is applied after pv-mongodb is applied.
step 9: We checked that the PVC is of status "BOUND" now and we can be sure that the data is persisted.
step 10.Alternatively another file mongodb-ss.yaml is also added to demostrate that the deployment could also be stateful with persistence volume attached to it.