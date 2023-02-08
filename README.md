# Project Structure
scgrp-17 is the final version which holds code to the part for the following
It has source code for both **microk8s and gke**.

**microk8s structure**: Please look into folders (mongo-db,certificates,ingress-tls)
* Persistence layer - mongodb yamal file with configmap and secrets - folder name (mongo-db)
* TLS self-signed certificates - folder name (certificates) for Ingress for the frontend and the api for microk8s - folder name (ingress-tls)
* RBAC in Microk8s in rbac folder

**gke link**
https://console.cloud.google.com/kubernetes/list/overview?project=eng-digit-375818
frontend running at http://34.70.78.14/  -(http://scapgrp.com/)
api for both get and post - http://104.197.247.205:5000/posts
which saves in momgodb that has a Pv of google dynamic provisioning.
**gke structure**
* This folder has all the code for gke 
* yaml files that are used to deploy
* managed certificates from google
* ingress for the LoadBalancer services
* network policies
* PVC
* Storage


## Presentation commands

### Network policies presentation

``` 

kubectl apply -f api-net-allow.yaml

kubectl apply -f db-net-allow.yaml

kubectl apply -f web-net-all.yaml

kubectl get networkpolicy

```



### RBAC presentation


```

microk8s enable rbac

openssl rand -base64 48

nano /var/snap/microk8s/current/credentials/known_tokens.csv

/var/snap/microk8s/current/credentials/known_tokens.csv

kubectl apply -f serviceaccount.yaml

kubectl get serviceaccount

kubectl create ns test-namespace

```


```

kubectl apply -f default-pod-reader-role.yaml 

kubectl apply -f readpod-rolebinding.yaml

kubectl auth can-i list pod --namespace default --as tom

kubectl auth can-i get pod --namespace default --as tom

kubectl auth can-i watch pod --namespace default --as tom

kubectl auth can-i create pod --namespace default --as tom

kubectl auth can-i delete pod --namespace default --as tom

```


```

kubectl apply -f cluster-secret-reader-role.yaml 

kubectl apply -f cluster-secret-reader.yaml 

kubectl auth can-i list secret --namespace default --as daniel

kubectl auth can-i get secret --namespace default --as daniel

kubectl auth can-i list pod --namespace default --as daniel

kubectl auth can-i get pod --namespace default --as daniel

```



```

kubectl apply -f cluster-deployment-role.yaml 

kubectl apply -f rolebinding-deployment.yaml 

kubectl auth can-i list deployment --namespace test-namespace --as alex

kubectl auth can-i create deployment --namespace test-namespace --as alex

kubectl auth can-i delete deployment --namespace default --as alex

kubectl auth can-i create deployment --namespace default --as alex

```



### Build, first deployment, scale delete presentation


```

kubectl apply -f mongodb-deployment/mongo-configmap.yaml

kubectl apply -f mongodb-deployment/mongo-secret.yaml

kubectl apply -f mongodb-deployment/mongodb-deployment.yaml

kubectl apply -f mongodb-deployment/pv-mongodb.yaml

kubectl apply -f mongodb-deployment/pvc-mongodb.yaml 

kubectl apply -f sns-api-deployment.yaml

kubectl get svc

```


```

sudo docker build . -t <dockerhub_id>/<repo>:v11

sudo docker push <dockerhub_id>/<repo>:v11

kubectl apply -f frontend-deployment.yaml

kubectl get svc

```


```

kubectl autoscale deployment sns-api-deployment --min=2 --max=5 --cpu-percent=60

kubectl autoscale deployment frontend-deployment --min=3 --max=5 --cpu-percent=80

kubectl get hpa

```


```

kubectl get deployment

kubectl delete deployment frontend-deployment -n default

kubectl delete deployment sns-api-deployment -n default

```



### Upgrade: rebuild, rollout, canary update presentation

```

sudo docker build . -t <dockerhub_id>/<repo>:v12

sudo docker push <dockerhub_id>/<repo>:v12

```

```

kubectl get pods --show-labels


kubectl --record deployment.apps/frontend-deployment set image deployment.v1.apps/frontend-deployment frontend-container=tzerok/frontendsns:v12

kubectl rollout status deployment/frontend-deployment

kubectl describe deployment frontend-deployment

```


```

kubectl get pods --show-labels

kubectl apply -f frontend-deployment-v2.yaml

kubectl scale --replicas=4 deploy frontend-deployment

kubectl get pods --show-labels

```
