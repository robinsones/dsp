#### Start the cluster!

```bash
/usr/local/hadoop/sbin/start-dfs.sh
```

Yes!!! It’s running. You can check the report on the cluster at this
address in your web browser:

```text
http://<YOUR_CLOUD_SERVER_IP>:50070
```

(Replace <YOUR_CLOUD_SERVER_ID> with the actual ip, like 167.214.312.54)   
You will also have to open port 50070 via aws security groups

On the terminal,

```bash
jps
```

will show you that `DataNode`, `NameNode` and `SecondaryNameNode` are running.


#### Let’s stop it

```bash
/usr/local/hadoop/sbin/stop-dfs.sh
```

Now go check

```text
http://<YOUR_CLOUD_SERVER_IP>:50070
```

It shouldn’t be there anymore!


#### Get data

Alright, let’s put some data in.

Let’s make a directory for these

```bash
mkdir /home/hduser/textdata
```

First we’ll start with putting the data into our normal data system.
If you have some text files on your ec2, you can use them for this.
If not, scp some data over from your local machine. 

```bash
cd ~/nltk_data/corpora/gutenberg
sudo scp melville-moby_dick.txt :~
```


Now on EC2: move the file to /home/hduser   


```bash
mv /home/username/melville-moby_dick.txt /home/hduser/
```

#### Put data in hdfs

First, let’s start the cluster again!

```bash
/usr/local/hadoop/sbin/start-dfs.sh
```

make some directories **in the hadoop distributed file system!**
(remember to update your username!)
```bash
cd (home)
hdfs dfs -mkdir /user/
hdfs dfs -mkdir /user/username/
hdfs dfs -mkdir /user/username/gutenberg
```

Let’s check that they exist

```bash
hdfs dfs -ls /
hdfs dfs -ls /user/
```

Yay!

Ok, put some data in

```bash
hdfs dfs -put /home/hduser/textdata/* /user/username/gutenberg
```

Check and make sure it is in the hdfs

```bash
hdfs dfs -ls /user/username
```

Yay!


#### Our mapper and reducer (use nano to create your your files)
### Note: Make sure you are in '/home/hduser'

Our mapper `mapper.py` includes the following code:

```python
#!/usr/bin/env python

import sys
from textblob import TextBlob

for line in sys.stdin:
    line = line.decode('utf-8')
    words = TextBlob(line).words
    for word in words:
        word = word.encode('utf-8')
        print "{}\t{}".format(word, 1)
```

And our reducer `count_reducer.py` looks like this:

```python
#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print '{}\t{}'.format(current_word, current_count)
        current_word = word
        current_count = count

if current_word == word:
    print '%s\t%i' % (current_word, current_count)
```

Before running this code, we need to make sure that textblob has its nltk corpora downloaded, so that it can work without an error. To do that, execute this on the command line (as the hduser):

```bash
python -m textblob.download_corpora
```


#### Let's run it!

Before giving the following command, don't forget to replace the `/user/username` path (in the hdfs) with your own version, and the paths to `mapper.py` and `count_reducer.py` (in your droplet's local filesystem) with your own versions.

chmod +x /home/hduser/mapper.py   
chmod +x /home/hduser/count_reducer.py

```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -file /home/hduser/mapper.py -mapper /home/hduser/mapper.py -file /home/hduser/count_reducer.py -reducer /home/hduser/count_reducer.py -input /user/username/gutenberg/melville-moby_dick.txt -output /user/username/book-output
```

Booom! :boom: It's running.


#### Looking at the output

Once it's done,

```bash
hdfs dfs -ls /user/username/book-output
```

should show that there is a `_SUCCESS` file (showing we did it!) and
another file called `part-00000`

This `part-00000` is our output. To look in:

```bash
hdfs dfs -cat /user/username/book-output/part-00000
```

or just

```
hdfs dfs -cat /user/username/book-output/*
```

will show the output of our job!

If you want to see the most common words, run:

```bash
hdfs dfs -cat /user/username/book-output/* | sort -rnk2 | less
```


######## Note:

If something went wrong when you ran your mapreduce job, you fix something and want to run it again, it will throw a different error, saying that the book-output directory already exists in hdfs. This error is thrown to avoid overwriting previous results. If you want to just rerun it anyway, you need to delete the output first, so it can be created again:

```bash
hdfs dfs -rm -r /user/username/book-output
```
