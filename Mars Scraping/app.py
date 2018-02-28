from flask import Flask, render_template, jsonify, redirect
#from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import scrape_mars

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = MongoClient('localhost', 27017)
db = client.mars

@app.route("/")
def index():
    scraper = [x for x in db.mars.find()]
    hemi_urls = [y.get("hemisphere") for y in scraper] #need this list comprehension to grab dictionary values
    return render_template("index.html", scraper=scraper, hemi_urls = hemi_urls)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    mars = db.mars
    mars.update({}, mars_data, upsert=True)
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
