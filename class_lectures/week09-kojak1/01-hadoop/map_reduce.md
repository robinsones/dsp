# Streaming map-reduce with Python

This example uses tweets as the data. The tweets were loaded into Python and then written to disk as stringified dicts. There are about 37 gigs of them at the `gadsdc-twitter` s3 bucket. For local demo purposes, [input.txt](input.txt) contains 25 tweets.

With simple [map](map.py) and [reduce](reduce.py) scripts, you can run locally:

```bash
cat input.txt | ./map.py | sort | ./reduce.py > output
```
