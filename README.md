# Networking Web Application with API

## Set Up ToDos

- Set up development environment DONE
- Build testing data
- Set up Mongo or SQL Server
- Create Login page
- Dockerize app

## Development

- Install application via docker-compose (phpmyadmin, mariadb, deployed app)

- Install portainer.io (Container managment)

`docker volume create portainer_data`  
`docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer`  

### OS Dependencies

- apt-get install php7.2-cli