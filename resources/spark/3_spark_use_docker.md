#Using Docker for Spark and Jupyter Notebook 

####Run the Docker Container
(It should not matter what directory you are in.  This is similar to wherever you usually open your Jupyter notebook.)
```bash
$ docker run -d -p 8888:8888 -v $PWD:/home/jovyan/work --name spark jupyter/pyspark-notebook
```

####Open Browser
Open a browser to [http://localhost:8888](http://localhost:8888) and you will see the Jupyter home page.

---
##Helpful Docker commands
####Check to see if any Docker processes running
```bash
reshama 🐘  $ docker ps
```

####Check all Docker processes
```bash
reshama 🐘  $ docker ps -a
```

####To remove a Docker proces
```bash
$ docker rm [name]
```

---

##References

[Docker error response from daemon: Conflict. already in use by container](http://stackoverflow.com/questions/31676155/docker-error-response-from-daemon-conflict-already-in-use-by-container)


