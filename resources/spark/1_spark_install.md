#Installing Spark :boom:
(Last updated:  8/19/16, Reshama)  

---

##Requirements:  Java
Check if Java is installed
```bash
reshama$ java -version
```
For me, it is not, so I will install from Java website:  
* Download site:  http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
* Accept license agreement  
* Choose appropriate file.  For me, it is:  `Mac OS X	227.35 MB  	jdk-8u102-macosx-x64.dmg`
* Install package by clicking on `*.dmg` file

####Confirm Java is installed by typing `java -version`
**Note:** you may need to open a new terminal window to see if the install is present.  
```bash
reshama$ java -version
java version "1.8.0_101"
Java(TM) SE Runtime Environment (build 1.8.0_101-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.101-b13, mixed mode)
reshama$ 
```

---

##Spark Download and Install

###Download Spark from this site:  http://spark.apache.org/downloads.html  
 * Choose a Spark release:  `1.6.2`
 * Download Spark: `spark-1.6.2-bin-hadoop2.6.tgz` (click on this file link and download)
 * Move Spark download to folder:  `user/myname/apps/`
 * `cd` into that folder:  `user/myname/apps/`
 * Expand the `spark-1.6.2-bin-hadoop2.6.tgz` file with this command:  `tar zxvf spark-1.6.2-bin-hadoop2.6.tgz`

####Example of my installation
```bash
reshama$ pwd
/Users/rshaikh/apps
reshama$ ls -Glp
total 0
drwxr-xr-x  3 rshaikh  staff  102 Apr 27 12:16 mongodb/
drwxr-xr-x  3 rshaikh  staff  102 Aug 15 12:31 spark/
reshama$ 
```
I have used `cd` to go into the `spark` folder:  
```bash
reshama$ pwd
/Users/rshaikh/apps/spark
reshama$ ls
spark-1.6.2-bin-hadoop2.6.tgz
reshama$ 
```
Next, expand the `*.tgz` file:  
```bash
reshama$ tar zxvf spark-1.6.2-bin-hadoop2.6.tgz
```

###Launch Spark Interactively by typing `bin/pyspark`:  
**Note:**  make sure you are in the appropriate directory.  
```bash
reshama$ pwd
/Users/rshaikh/apps/spark/spark-1.6.2-bin-hadoop2.6.tgz
reshama$ bin/pyspark
```  

###Example of what interactive spark looks like once launced
```bash
reshama$ bin/pyspark
Python 2.7.6 (default, Sep  9 2014, 15:04:36) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel).
16/08/15 13:11:34 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.2
      /_/

Using Python version 2.7.6 (default, Sep  9 2014 15:04:36)
SparkSession available as 'spark'.
>>> 
```
###Confirm spark context is there by typing `sc`:  
```bash
>>> sc
<pyspark.context.SparkContext object at 0x107083e50>
```
###More code to test:  
```spark
>>> input = [1, 2, 3, 4, 5]
>>> input
[1, 2, 3, 4, 5]
>>> type(input)
<type 'list'>
>>> 
```

###To exit interactive Spark, type `exit()`:   
```bash
>>> exit()
reshama$ 
```

:boom: :boom: :boom: **Congrats on a successful install!  You are now running interactive Spark -- with Python!** :boom: :boom: :boom:

---

####References
* [Getting Started with Spark in Python](https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python)
* [Configuring IPython Notebook for PySpark](http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/)
 
