# Custom Docker Flask Deployment Image
# docker build . -t flask_image
# docker run --name flask_container -p 80:80 flask_image
# Review HTTPS configurations
FROM python:3.6-slim

COPY . /srv/flask_app
WORKDIR /srv/flask_app

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]
