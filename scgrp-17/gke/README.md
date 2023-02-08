# This folder contains the db yaml files needed for deployment in gke.
*GCP project link is below
The cluster name is fancy-cluster.

https://console.cloud.google.com/kubernetes/clusters/details/us-central1-f/fancy-cluster/details?project=eng-digit-375818

* The post data could be validated in the below link
http://104.197.247.205:5000/posts

Which fetches and posts the data to mongodb using restapi.


* The managed certificates from google and the ingress for the frontend.
* The network policies that are applied in GKE is in the folder network-policies.
* Rest api running on Load balancer
