
####`cd` to `spark-docker` folder
```bash
reshama 🐘  $ pwd
/Users/reshamashaikh/apps/spark-docker
reshama 🐘  $ 
```

####Run the Docker Container
```bash
$ docker run -d -p 8888:8888 -v $PWD:/home/jovyan/work --name spark jupyter/pyspark-notebook
```


