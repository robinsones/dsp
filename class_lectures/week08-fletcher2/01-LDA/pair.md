#### Pair Problem

You are given documents as probability distributions over topics, and topics as probability distributions over words.

Implement a function `make_doc` that takes a document (as `topic_probs`) and a number of words. The function should randomly generate a document by choosing a topic for each word using the document's topic probabilities and then choosing a particular word using that topic's word probabilities. The function should return a string containing all the generated document's words.

For example:

```python
docs = [[0.98, 0.01, 0.01],
        [0.01, 0.98, 0.01],
        [0.01, 0.01, 0.98]]
topics = [[ 0.4,      0.4,   0.01,        0.01,    0.01,       0.01,
            0.1,     0.04,   0.01,        0.01],
          [0.01,     0.01,    0.4,         0.4,    0.01,       0.01,
            0.1,     0.04,   0.01,        0.01],
          [0.02,     0.02,   0.01,        0.01,     0.4,        0.4,
           0.02,      0.1,   0.01,        0.01]]
words =  ['cat', 'kitten',  'dog',     'puppy',  'deep', 'learning',
          'fur',  'image',  'GPU', 'asparagus']


def make_doc(topic_probs, n_words):
    raise NotImplementedError

for doc in docs:
    print make_doc(topic_probs=doc, n_words=10)

#  Example output:
## cat learning kitten image kitten cat deep image cat kitten
## puppy puppy learning dog puppy dog dog puppy image dog
## deep learning deep image deep deep deep deep learning learning
```

Extension:

Update your `make_doc` function so that if `topic_probs` isn't specified, it will draw a random set of topic probabilities from a Dirichlet distribution.
