#!/bin/sh

templater ./service.yml | kubectl apply -f -
templater ./ingress.yml | kubectl apply -f -
# templater ./pvc.yml | kubectl apply -f -
templater ./deployment.yml | kubectl apply -f -

kubectl -n $NAMESPACE rollout status deployment ${SERVICE_NAME}-${ENV}-deployment

echo "Deployment finished url is in ..."

kubectl -n $NAMESPACE get ing