#Spark Resources

##RDD Operations

Transformations | Actions 
--- | --- 
*lazy*  | *executing* 
**map(func):** pass each element of source through func, return new RDD | **reduce(func):** aggregate elements with func
**filter(func):** select elements of the source for which func returns true, return new distributed RDD | **take(n):** copy top n elements to driver
**distinct():** return duplicate-free RDD | **collect():** copy all elements to driver
**sample(withReplacement, fraction [seed]):** sample RDD, with or without replacement |  **foreach(func):** apply provided func to each element of RDD
[more Transformations](http://spark.apache.org/docs/latest/programming-guide.html#transformations) | [more Actions](http://spark.apache.org/docs/latest/programming-guide.html#actions)

##RDD:  Sample Execution Plan

Item | Step |   |  | 
---- | ---- |----|----| 
1   | Create RDD from text file             | RDD            | `sc.textFile(“/dirpath/textfile.txt”)`  
2   | Flattens lists of words into one list  | `flatMap`      | `.flatMap(lambda x: x.split())`
3   | Remove punctuation, convert to upper case  | `.map()`   | `.map(lambda x: x.replace('|', '').replace('.', '').replace('-', '').replace(' ', '').replace('&', '').replace('#','').upper())`
4   | Word count **mapper** function            | `.map()`       | `.map(lambda x: (x, 1))`
5   | Word count **reducer** function           | `.reducer()`   | `.reduceByKey(lambda a, b: a + b)`   `.sortByKey(ascending=False)`
6a  | return RDD pipeline - all items       | `collect()`    |  `.collect()`
6b  | return RDD pipeline - 10 items        | `take()`       | `.take(10)`
6c  | return RDD pipeline - first item      | `first()`      | `.first()`





---

##Resources

####Recommended Books
* [Learning Spark](http://shop.oreilly.com/product/0636920028512.do)
* [Advanced Analytics with Spark](http://shop.oreilly.com/product/0636920035091.do)

####[Databricks](https://databricks.com/)  
* Founded out of the UC Berkeley AMPLab by the team that created Apache Spark.  
* Explore the [Databricks cloud environment](https://databricks.com/product/getting-started-with-apache-spark-on-databricks)

####What's Next, after Spark:  Scala
* [Scala](http://www.scala-lang.org/index.html) is an acronym for “Scalable Language”. This means that Scala grows with you. You can play with it by typing one-line expressions and observing the results. But you can also rely on it for large mission critical systems, as many companies, including Twitter, LinkedIn, or Intel do.
* [Scala tutorial](http://www.tutorialspoint.com/scala/)
  

