# How to deploy mongodb

* step 1. First apply the command:
kubectl apply -f mongo-configmap.yaml
* step 2.Then in the same way apply mongo-secret.yaml
* step 3.Now its time to apply the mongodb-deployment.yaml in the same way.
* step 4.When the database is deployed using the previous command ,it creates both the deployment and service in Kubernetes.
* step 5.Now we can deploy our web application , for demo a web-client for mongo-db is added here which is mongo-express.yaml which should be replaced by the web-application of the project.Here it is used as a demo to check the database which offcourse could also be done from the terminal.
* step 6. Congigure **Ingress with TLS Certificate** . Here mongo-express is used to configure ingress,which could easily be replace by the web-application.
* step 7.Persistence Volume : The file pv-mongodb.yaml has configuration for Persistence Volume for mongodb,the storage class is microk8s-hostpath which is mapped to local path in a VM : /opt/mongodb/data
First PV is created by allowcating a volume of type:hostPath and then the following PVC is applied.
* step 8.File pvc-mongodb.yaml is applied after pv-mongodb is applied.
* step 9: We checked that the PVC is of status "BOUND" now and we can be sure that the data for mongodb is persisted.
* step 10.Alternatively another file **mongodb-ss.yaml** is also added to demostrate that the deployment could also be of type **Stateful** with persistence volume attached to it in a similiar way.Either of the two files **mongodb-ss.yaml** or **mongodb-deployment.yaml** could be used to deploy the database.
