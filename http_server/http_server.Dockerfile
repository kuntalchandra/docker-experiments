FROM ubuntu:18.04
RUN apt update -y
RUN apt install -y vim
RUN apt install -y python3.8
RUN apt install -y sudo
RUN useradd http_server_user -p 'ephemeral' -u 1001 -m
RUN passwd -d http_server_user
RUN usermod -aG sudo http_server_user
USER http_server_user
WORKDIR /home/http_server_user/src
ENV PORT=8888
EXPOSE 8888 
