from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/gallery/<photo>')
def photo(photo):
    template = 'photo_' + photo +'.html'
    return render_template(template)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)