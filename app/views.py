import os
from app import app

#image libraries
from PIL import Image
import cv2
import numpy as np

from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """



app.config["IMAGE_UPLOADS"] = "/mnt/c/wsl/projects/pythonise/tutorials/flask_series/app/app/static/img/uploads"
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            #now that we have the image, we should be able to send it to the model
            image = request.files["image"]

            read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
            img = read(image)
            img = cv2.resize(img, (224,224))

            img = np.array(img)/255.
            img = np.array(img)/255.
            img = np.reshape(img,[1,224,224,3])
            
            #print(image)

            return redirect(request.url)


    
    return render_template("public/upload_image.html", user_image = image) if (request.method == "POST") else render_template("public/upload_image.html")