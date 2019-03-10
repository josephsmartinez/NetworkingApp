# Networking Web Application with API

## Set Up ToDos

- Set up development environment DONE
- Build testing data
- Set up Mongo or SQL Server DONE
- Create Login page DONE
- Dockerize app
- Config Athenication
- Update login process
- Update views
- Index json data to sql
- Create view for past requests
- Log GET and POST request
- Intergrade other APIs if possible

## Resources

https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#connecting
https://docs.python.org/2.5/lib/sqlite3-Cursor-Objects.html
https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
http://flask-sqlalchemy.pocoo.org/2.3/api/
https://docs.sqlalchemy.org/en/latest/orm/session_basics.html
https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy
http://exploreflask.com/en/latest/static.html
https://getbootstrap.com/docs/4.0/getting-started/introduction/
https://snipe-it.readme.io/v4.0/reference#hardware-list
https://github.com/jbloomer/SnipeIT-PythonAPI

## Development

- Install application via docker-compose (phpmyadmin, mariadb, deployed app)

- Install portainer.io (Container managment)

`docker volume create portainer_data`  
`docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer`  

## OS Dependencies

- apt-get install php7.2-cli

## Python Vitual Environment

Install with pip or pip3  
`pip3 install virtualenv`  
Create env  
`virtualenv venv --python=python3.6`  
Start env  
`source venv/bin/activate`  
Stop env  
`deactivate`  
List installed package and libraries  
`pip freeze`  
To upgrade all local packages  
`pip install pip-review`  
`pip-review --local --interactive`  
