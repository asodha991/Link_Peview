import pickle
from pydoc import describe
from flask import Flask, request, app, jsonify,url_for, render_template
from matplotlib.image import thumbnail
from matplotlib.pyplot import title
import numpy as np
from utility import generate_preview 


app = Flask (__name__)


@app.route("/")

def home():
    return render_template('index.html')

@app.route('/run', methods= ['POST'])

def run():
    output = request.form.to_dict()
    url = output["url"]
    description, thumbnail,title, urls  = generate_preview(url)
  
    preview_html = render_template('index.html',URL = url,URLS = urls, Title = title, Thumbnail= thumbnail, Description = description)

    return (preview_html)


if __name__ == "__main__":
    app.run()

