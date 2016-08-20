#IPython Notebook Configuration with PySpark

* One way to configure your IPython Notebook with your *local* installation of Spark is detailed in the blog   
[Configuring IPython Notebook for PySpark](http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/).  
* However, there are lots of details that make it time-intensive for trouble-shooting.  
* Fortunately, there is an easier option:  Docker.  

##About Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

In a way, **Docker is a bit like a virtual machine.** But unlike a virtual machine, rather than creating a whole virtual operating system, Docker **allows applications to use the same Linux kernel as the system that they're running on** and only requires applications be shipped with things not already running on the host computer. This gives a significant performance boost and reduces the size of the application.

And importantly, Docker is open source. This means that anyone can contribute to Docker and extend it to meet their own needs if they need additional features that aren't available out of the box.

---

We will be using this blog for the next steps:  [Quick-start Apache Spark Environment Using Docker Containers](http://maxmelnick.com/2016/06/04/spark-docker.html)

##Install Docker

Follow the instructions in the install / get started links for your particular operating system:  
  * Mac: https://docs.docker.com/docker-for-mac/
  * Windows: https://docs.docker.com/docker-for-windows/
  * Linux: https://docs.docker.com/engine/getstarted/

##Run Docker

Follow the instructions in the section:  *Run the Docker Container*

##Run Jupyter Notebook Using PySpark

Follow the instructions in the section:  *Test Spark in a Jupyter notebook using Pyspark*

Also, review this section:  *Starting and stopping the Docker container*

Congratulations!  You have used one of the hottest tools in cloud computing, Docker.  And, you are able to use PySpark in  Jupyter Notebook!  

---

####References
* [What is Docker](https://opensource.com/resources/what-docker)
* [What is Docker and Why is it so Darn Popular](http://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)
* [Quick-start Apache Spark Environment Using Docker Containers](http://maxmelnick.com/2016/06/04/spark-docker.html)

