from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)