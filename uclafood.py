import os 
#import psycopg2
import urlparse 
#module for building webapps
from flask import Flask, url_for, render_template, request
import requests
#module for processing html and xml 
import bs4
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
  scraper()

if __name__ == "__main__":
  app.run()


