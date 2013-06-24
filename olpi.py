#!/usr/bin/env python

import sys, datetime, time, flask
from flask import Flask

app = Flask(__name__)

def event_stream():
	count = 0
	#yield 'hejsan'
	while True:
		count += 1
		yield "data: Button press #%d @ %s\n\n" % (count, datetime.datetime.now())
		time.sleep(1)

@app.route('/stream')
def stream():
	return flask.Response(event_stream(), mimetype="text/event-stream")# "text/event-stream")

@app.route("/")
def hello():
	return """
        	<!doctype html>
	        <html>
	          <head>
	            <title>RPi SSE Test</title>
	            <script>
	                function sse() {
	                    var source = new EventSource('/stream');
        	            source.onmessage = function(e) {
	                        var out = document.getElementById('out');
	                        out.innerHTML =  '  <li>'+ e.data + '</li>' + out.innerHTML;
                	    };
	                }
	                sse();
	            </script>
	          </head>
	          <body>
		    <h1>SSE-Test</h1>
	            <ul id="out"></ul>
	          </body>
	        </html>
	    """

if __name__ == "__main__":
    app.run('0.0.0.0',5001)
