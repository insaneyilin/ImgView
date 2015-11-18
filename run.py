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
parser.add_argument('-p', '--path', default="", type=str, help="Path of image directory.")
args = parser.parse_args()
image_dir = args.path

image_dir = os.path.abspath(image_dir)
app = Flask(__name__, 
            static_url_path = '', 
            static_folder = image_dir)
app.debug = True

@app.route("/index")
def index():
    types = ["*.png", "*.jpg", "*.JPG"]
    image_list = []
    for cur_type in types:
        image_list.extend(glob.glob(os.path.join(image_dir, cur_type)))
    image_list = [url_for("static", filename=os.path.basename(x)) for x in image_list]
    return render_template("index.html", image_list = image_list)

app.run(host='0.0.0.0', port=8070, threaded=True) 

