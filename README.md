# Docker-Icecast2

Procedures basics for use **Icecast2**

# Execute Icecast2

First download the image from DockerHub

```shell
docker pull danielm1999/icecast2
docker run -p 8000:8000 icecast2
```

Then create a yml file. Example name-any.yml and enter the following code:

```yml
version: '3'
services:
        icecast:
                image: danielm1999/icecast2
                environment:
                        - IC_ADMIN=daniel
                        - IC_PASSWORDADMIN=hackme
                        - IC_CLIENTES=100
                        - IC_SOURCES=2
                        - IC_QUEUESIZE=524288
                        - IC_CLITIMEOUT=30
                        - IC_HEADERTIMEOUT=15
                        - IC_SOURCETIMEOUT=10
                        - IC_BURSTCONNECT=1
                        - IC_BURSTSIZE=65535
                        - IC_IP=localhost
                        - IC_PORT=8000
                ports:
                        - "8000:8000"
```

In this file you can change the information you prefer.

After yml is created, type the following commands in the terminal:

```shell
docker swarm init
docker stack deploy -c name-any.yml (**a name you want**)
```

The following table shows what each variable changes in icecast.xml

| **Variable** | **Function** | **Standard Value** |
| :----------- | :----------- | :----------------- |
| IC_ADMIN     | change admin for icecast admin access | daniel |
| IC_PASSWORDADMIN | change admin password | hackme |
| IC_CLIENTES | change limit of clients that will access the server | 100 |
| IC_SOURCES | change font limit | 2 |
| IC_QUEUESIZE | change the maximum size (in bytes) of the stream queue | 524288 |
| IC_CLITIMEOUT | change the time the user is logged on to the server | 30 |
| IC_HEADERTIMEOUT | change the maximum time (in seconds) to wait to receive a request | 15 |
| IC_SOURCETIMEOUT | change (in seconds) if the source is not sending audio to be removed from the server | 10 |
| IC_BURSTCONNECT | when enabled, the burst size is 64 kbytes and off, the burst size is 0 kbytes | 1 |
| IC_BURSTSIZE | change the size of the amount of data (in bytes) to be intercepted on a client at the time of connection. | 65535 |
| IC_IP | change ip address | localhost | 
| IC_PORT | change the door | 8000 |

