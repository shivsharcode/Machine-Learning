

from flask import Flask, render_template, request, redirect, url_for
from model import suggest_movies


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', suggestions=None)


@app.route('/submit', methods=['POST', 'GET'])
def movie_input():
    user_input_movie = ""
    if request.method == 'POST':
        user_input_movie = request.form['movie']
        
        suggestions = suggest_movies(user_input_movie)
        return render_template('index.html', suggestions= suggestions)
    
    return redirect(url_for('home'))

if __name__ == '__main__' : 
    app.run(debug=True)