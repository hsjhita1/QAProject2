#!/bin/bash
env PROJECT2_DB="${PROJECT2_DB}" docker stack deploy -c docker-compose.yaml services