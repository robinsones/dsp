import flask
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main_page():
    with open("index.html", 'r') as viz_file:
        return viz_file.read()


from sklearn.cluster import KMeans
import numpy as np

@app.route("/cluster", methods=["POST"])
def cluster():
	
	data = request.json
	data = data['coords']

	n_clusters = data.pop()
	length = len(data)
	if n_clusters>length/2:
		n_clusters = length/2

	if length==0:
		return
	
	x,y = np.array(data[:length/2]),np.array(data[length/2:])

	X = np.hstack((x[:,None],y[:,None]))

	kmeans = KMeans(n_clusters=n_clusters, init='k-means++', n_init=100, 
					max_iter=300, tol=0.0001, precompute_distances='auto')

	res = {}
	res['assignments'] = kmeans.fit(X).labels_.tolist()

	return flask.jsonify(res)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=port)
