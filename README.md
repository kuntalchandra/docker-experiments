# Build local development environments using Docker containers
- Understand Docker basic commands
- Use an Ubuntu Docker image to create an independent Ubuntu container
- Build a custom image for the HTTP server
- Build a custom container for the HTTP server
- Run a custom container and create the HTTP server
- Build the API server using a separate development environment
- Use Docker Compose to make the two servers communicate
- Build images using Docker Compose and final adjustments

## Purpose
- To remind myself how it all started. And, also keep it backed up.

### Basic commands
- `$ docker run --name example_container hello-world`
- `$ docker images`
- `$ docker container ls -a`
- `$ docker rm f5ac855a31b0`
- `$ docker rmi 61941b2`
- `$ docker pull ubuntu`
- `$ docker create -it --name sample_ubuntu_container ubuntu`
- `$ docker start sample_ubuntu_container`
- `$ docker attach sample_ubuntu_container`
- `$ docker port http_server`
- `$ docker-compose up -d` 
- `$ docker-compose down` 