### mongoDB

To install mongoDB on Ubuntu, follow the [directions](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/) in the manual:

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update
sudo apt-get install -y mongodb-org
```

This will install _and start up_ mongoDB. You can check:

```bash
ps awx | grep mongo
```

On Ubuntu, servers are started and stopped mostly with [upstart](http://upstart.ubuntu.com/). Try:

```bash
sudo service mongod status
sudo service mongod stop
sudo service mongod start
```

Connect to the mongoDB server with `mongo`.

```
help
show dbs
use new_cool_db
show dbs
```

mongoDB is lazy about making things, which is usually a good thing.

```
j = { name: "Eddie" };
k = { name: "Felicity" };
l = { nationality: "British" };
db.testData.insert(j);
db.testData.insert(k);
db.testData.insert(l);
show dbs
show collections
```

Very JavaScript.

```
db.testData.find();
td = db.testData;
td.find();
```

`find` returns a cursor:

```
var c = td.find();
while ( c.hasNext() ) { printjson( c.next() ) }
```

You can search for things!

```
td.find( {x: { $lt: 20 } } );
td.find( {name: { $lt: 'F' } } );
```

Let's put more things in mongo:

```
for (var i=1; i<=25; i++) {
    td.insert( {x : i } );
}
td.find();
it  // iterate
```

Now we can do some more interesting [queries](http://docs.mongodb.org/manual/tutorial/query-documents/):

```
td.find( {x: {$lt : 20 } } );
td.find({$or: [
               { name: "Eddie"},
               {x: { $gt : 22 } }
              ]
});
```

Now, with Python! If you don't have `pymongo` installed, you can `sudo pip install pymongo`.

```python
from pymongo import MongoClient

client = MongoClient()
db = client.my_cool_database

db.collection_names()
col = db.my_cool_collection

```

Trying out the data from the challenges:
```
scp heavy_metal_parsed.pkl ubuntu:~
```

```python
from pymongo import MongoClient
client = MongoClient()

import pickle
with open('heavy_metal_parsed.pkl', 'r') as infile:
    reviews = pickle.load(infile)
reviews[0].keys()
reviews[0]
len(reviews)

hmm = client.my_cool_db.hmm
hmm.insert(reviews[0])
hmm.find().next()

for review in reviews[1:]:
    hmm.save(review)

cursor = hmm.find()
len(list(cursor))  # don't do this!
hmm.count()        # do this instead!
```
