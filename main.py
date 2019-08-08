from flask import Flask, render_template, request
import urllib.request
import json



app = Flask(__name__)


@app.route('/')
def home():
    url = 'https://api.nasa.gov/planetary/apod?api_key='
    key = 'fOrNYkZMYt8KEwieCkuEcYJi3uMYQvQpvDDFjEmv'
    urlobj = urllib.request.urlopen(url + key)
    read = urlobj.read()
    decode = json.loads(read.decode('utf-8'))
    image = decode['url'
    return render_template('layout.html', image=image)
@app.route('/key', methods=['POST'])
def key():
    key = request.form['apikey']
    image = buildURL(url, key)
    return render_template('layout.html', image=image)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
