# Kubernetes Operator demo

This repo contains 2 services:
- A very simple API in `simple_api` folder
- A proof of concept k8s oprator in `operator_api` folder

## Operator
A proof of concept kubernetes operator using `kopf` python framework.
Actions are just calling the `simple_api` service in the cluster.
Manifests folder contains all required SA, CRD, etc.

## Api

Very simple Flask based Api exposes 2 endpoints: 
- `/update`
- `/delete`

Each of them just logs out the action, and the payload that was sent to them.