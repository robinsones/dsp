#IPython Notebook Configuration with PySpark

One way to configure your IPython Notebook with your *local* installation of Spark is detailed in the blog   
[Configuring IPython Notebook for PySpark](http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/).  However, there are lots of details that make it time-intensive for trouble-shooting.  Fortunately, there is an easier option:  Docker.  

##Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

In a way, **Docker is a bit like a virtual machine.** But unlike a virtual machine, rather than creating a whole virtual operating system, Docker **allows applications to use the same Linux kernel as the system that they're running on** and only requires applications be shipped with things not already running on the host computer. This gives a significant performance boost and reduces the size of the application.

And importantly, Docker is open source. This means that anyone can contribute to Docker and extend it to meet their own needs if they need additional features that aren't available out of the box.







---

####References
* [What is Docker](https://opensource.com/resources/what-docker)
