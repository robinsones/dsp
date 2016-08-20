
####`cd` to `spark-docker` folder
```bash
reshama 🐘  $ pwd
/Users/reshamashaikh/apps/spark-docker
reshama 🐘  $ 
```

####Copy spark notebook and data (from nyc16_ds8 repo) into this folder
```bash
reshama 🐘  $ pwd
/Users/reshamashaikh/apps/spark-docker
reshama 🐘  $ ls -Glp
total 224
drwxr-xr-x  10      340 Aug 19 22:04 spark_data/
-rw-r--r--   1   107853 Jun 23 16:59 spark_functions_ml.ipynb
reshama 🐘  $ 
```
####Check to see if any Docker processes running
```bash
eshama 🐘  $ docker ps
```

####Run the Docker Container
```bash
$ docker run -d -p 8888:8888 -v $PWD:/home/jovyan/work --name spark jupyter/pyspark-notebook
```

