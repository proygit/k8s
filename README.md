# Project Structure
scgrp-17 is the final version which holds code to the part for the following
It has source code for both **microk8s and gke**.

**microk8s structure**: Please look into folders (mongo-db,certificates,ingress-tls)
* Persistence layer - mongodb yamal file with configmap and secrets - folder name (mongo-db)
* TLS self-signed certificates - folder name (certificates) for Ingress for the frontend and the api for microk8s - folder name (ingress-tls)

**gke structure**
* This folder has all the code for gke 
* yaml files that are used to deploy
* managed certificates from google
* ingress for the LoadBalancer services
* network policies
*  PVC
* Storage
