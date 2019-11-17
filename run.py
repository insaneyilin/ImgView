#!/usr/bin/env python
import os
import sys
import json
import fnmatch
import glob
from flask import Flask, g, url_for
from flask import render_template, request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', default="", type=str, help="Path of image directory.")
parser.add_argument('-p', '--port', default="8000", type=int, help="Port.")
args = parser.parse_args()
image_dir = os.path.abspath(args.dir)
port = args.port
app = Flask(__name__, 
            static_url_path = '', 
            static_folder = image_dir)
app.debug = True

@app.route("/")
def index():
    types = ["*.png", "*.jpg", "*.JPG"]
    image_list = []
    for cur_type in types:
        image_list.extend(glob.glob(os.path.join(image_dir, cur_type)))
    image_list = [url_for("static", filename=os.path.basename(x)) for x in image_list]
    image_list = json.dumps(image_list)
    return render_template("index.html", image_list = image_list)

app.run(host='0.0.0.0', port=port, threaded=True) 

