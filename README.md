# Graph Builder

This is a flask webapp that interfaces with a NetworkX (NX) graph object.

NX effectively acts as middleware (webservice) (see graphgen.py), while flask provides the webapp.

Below are the middleware options.  

## graphgen (fast, for python-native server application)
This is the NX graph object with addtional properties. This can be imported by the flask app and manipulated there. It is the NX API (plus our additions) that is consumed by the flask webapp. This project will be using this option.

## graphbuilder (slow, for non-native server application (JSON API))
This an alternative to `graphgen` but much slower, as it generates and consumes JSON graph data. This provides cross-platform interoperability between the NX graph object and another non-python server.   

There is also the option of running graphbuilder as a subprocess and keeping it open, while writing to it via stdin, which may be faster than the current JSON approach (which involves loading JSON, construction a graph from JSON, updating the graph, and renegerating that JSON).