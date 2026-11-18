#!/bin/bash

# nginx1 et nginx2 ont --rm : ils sont supprimés automatiquement à l'arrêt
docker stop nginx1 nginx2 nginx-lb

# nginx-lb n'a pas --rm : on le supprime explicitement
docker rm nginx-lb

# Suppression du réseau (en dernier : il doit être vide)
docker network rm tplb
