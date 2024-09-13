# running simple Flask webapp application

We can try below steps on ubuntu image before we dockerize the applcation

## Steps to follow to make the applicaiton run in ubuntu image

apt update

apt install -y python3 python3-setuptools python3-dev build-essential python3-pip python3-mysqldb

pip3 install flask --break-system-packages

pip3 install flask-mysql --break-system-packages

--> create a app.py file and copy the content from app.py file in this directory

and now finally run the application:

FLASK_APP=/opt/app.py flask run --host=0.0.0.0


## to dockerize this, we need to create the dockerfile as above and then run it

docker build .