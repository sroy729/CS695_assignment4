#Docker container migration 
The aim of the project to checkpoint and migrate docker container and have evaluate there performance

##How to checkpoint 

```bash
docker run -d --name looper2 busybox \
         /bin/sh -c 'i=0; while true; do echo $i; i=$(expr $i + 1); sleep 1; done'

docker checkpoint create --checkpoint-dir=/tmp looper2 checkpoint2

mv /tmp/checkpoint2 /var/lib/docker/containers/$(docker ps -aq --no-trunc --filter name=looper2)/checkpoints/

docker start --checkpoint=checkpoint2 looper2
```

We were able to ckeckpoint and restore docker container 


##Observation 

We tried to checkpoint a running server client relationship. The server was running inside a docker container and the client was
running on a different system that is on the same intranet with the server.

We noticed that when there is a active connection happpening between server and the client the checkpoint mechanism fails to 
checkpoint server docker container. But when the server is serving no request it is easily checkpointable.

**Reason**
we think that the possible reason for this is when docker is remapping the port the checkpointing mechansim is not able to break the 
mapping and hence fails to checkpiont

##Scope

- We were able to checkpoint docker container that is running a single process
- We are able to checkpoint docker container that is running multiple processes.
- We are able to resume from checkponit in the same machine or in another machine that

#Experiments

- Downtime for migrating

