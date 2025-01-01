# from ubuntu
# run apt-get update
# run apt-get install -y python3 python3-pip
# run apt install -y python3-flask
# run mkdir /opt/app

# workdir /opt/app

# # copy app.py /opt/app/app.py
# copy . /opt/app

# # entrypoint FLASK_APP=/opt/app/app.py flask run --host 127.0.0.1
# cmd ["python3","app.py"]


from ubuntu
run apt-get update
run apt-get install -y python3 python3-pip
run apt install -y python3-flask
run mkdir /opt/app

workdir /opt/app

copy . /opt/app

entrypoint FLASK_APP=/opt/app/app.py flask run --host 0.0.0.0


# cmd ["python3","app.py"]

# entrypoint [ "python3" ]
# entrypoint [ "python3" ,"app.py"]
# cmd ["app.py"]


