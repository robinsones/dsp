#Spark

Transformations | Actions 
--- | --- 
*lazy*  | *executing* 
**map(func):** pass each element of source through func, return new RDD | **reduce(func):** aggregate elements with func
**filter(func):** select elements of the source for which func returns true, return new distributed RDD | **take(n):** copy top n elements to driver
**distinct():** return duplicate-free RDD | **collect():** copy all elements to driver
**sample(withReplacement, fraction [seed]):** sample RDD, with or without replacement |  **foreach(func):** apply provided func to each element of RDD
[more Transformations](http://spark.apache.org/docs/latest/programming-guide.html#transformations) | [more Actions](http://spark.apache.org/docs/latest/programming-guide.html#actions)





---

####Recommended Books
* [Learning Spark](http://shop.oreilly.com/product/0636920028512.do)
* [Advanced Analytics with Spark](http://shop.oreilly.com/product/0636920035091.do)

---

####What's Next, after Spark:  Scala
* [Scala](http://www.scala-lang.org/index.html) is an acronym for “Scalable Language”. This means that Scala grows with you. You can play with it by typing one-line expressions and observing the results. But you can also rely on it for large mission critical systems, as many companies, including Twitter, LinkedIn, or Intel do.
* [Scala tutorial](http://www.tutorialspoint.com/scala/)
  
