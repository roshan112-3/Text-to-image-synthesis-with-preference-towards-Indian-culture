from flask import Flask, render_template, request, redirect, url_for
import requests
import io
from PIL import Image

app = Flask(__name__)

API_URL1 = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
API_URL2 = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_URL3 = "https://api-inference.huggingface.co/models/Ashish08/vada-sambhar-south-indian-dish"
headers = {"Authorization": "Bearer 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"}

def query(API_URL, payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content


@app.route('/', methods=['GET', 'POST'])
def index():
    image = None
    if request.method == 'POST':
        text = request.form['text']
        image_bytes = query(API_URL1, {"inputs": text})
        image = Image.open(io.BytesIO(image_bytes))
        image = image.save("/Users/nrpartheev/Desktop/MMDS/static/image1.jpg") 

        image_bytes = query(API_URL2, {"inputs": text})
        image = Image.open(io.BytesIO(image_bytes))
        image = image.save("/Users/nrpartheev/Desktop/MMDS/static/image2.jpg") 

        image_bytes = query(API_URL3, {"inputs": text})
        image = Image.open(io.BytesIO(image_bytes))
        image = image.save("/Users/nrpartheev/Desktop/MMDS/static/image3.jpg") 
        return render_template('index.html', count=1)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
