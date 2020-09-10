FROM node:12.18-slim
RUN apt update -y
RUN apt install -y vim
RUN apt install -y sudo
RUN passwd -d node
RUN usermod -aG sudo -u 1001 node
USER node
WORKDIR /home/node/src
CMD ["/bin/bash"]
ENV PORT=12345
EXPOSE 12345 
