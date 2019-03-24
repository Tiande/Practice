FROM ubuntu
COPY sources.list /etc/apt/ 
COPY .bashrc /root/
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean
