from flask import Flask, render_template
import pandas as pd
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
data = pd.read_csv(url)

url2 = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
data2 = pd.read_csv(url2)


@app.route('/about')
def hello_world():
    return 'Hello, World'

url4 = "https://www.youtube.com/watch?v=NuTAgztj_NI"
data4 = requests.get(url)

@app.route('/')
def about():
    return render_template('about.html', data=data, data2=data2, data4=data4)

    

if __name__ == '__main__':
    app.run(debug=True)