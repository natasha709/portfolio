from flask import Flask, render_template
import webbrowser
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def open_chrome():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    if os.path.exists(chrome_path):
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open('http://127.0.0.1:5000')
    else:
        # Try alternative Chrome paths
        alternative_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        if os.path.exists(alternative_path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(alternative_path))
            webbrowser.get('chrome').open('http://127.0.0.1:5000')
        else:
            print("Chrome not found in standard locations. Opening in default browser.")
            webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000')
    app.run(debug=True)
