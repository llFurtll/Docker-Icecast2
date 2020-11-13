FROM debian:latest

RUN apt-get update && \
    apt-get full-upgrade --yes && \
    apt-get install icecast2 python3 sudo --yes && \
    chown -R icecast2 /etc/icecast2 

EXPOSE 8000

VOLUME ["/cert1", "/privkey1"]

ADD ./cert1.pem /cert1.pem
ADD ./privkey1.pem /privkey1.pem

CMD cat /cert1.pem /privkey1.pem > /etc/icecast2/bundle.pem && chmod 777 /etc/icecast2/bundle.pem


ENV IC_CLIENTES "100"
ENV IC_SOURCES "42"
ENV IC_QUEUESIZE "524288"
ENV IC_CLITIMEOUT "30"
ENV IC_HEADERTIMEOUT "15"
ENV IC_SOURCETIMEOUT "10"
ENV IC_BURSTCONNECT "1"
ENV IC_BURSTSIZE "65535"
ENV IC_SOURCEPASSWORD "hackme"
ENV IC_ADMIN "admin"
ENV IC_PASSWORDADMIN "hackme"
ENV IC_IP "localhost"
ENV IC_PORT "8000"

VOLUME ["/var/log/icecast2", "/config", "/etc/icecast2"]

ADD ./etc /etc
ADD ./config.py /config.py
ADD ./init.sh /init.sh

CMD sh /init.sh
