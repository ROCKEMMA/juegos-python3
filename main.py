from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de ejemplo
@app.route('/about')
def about():
    return "<h1>Página About</h1>"

if __name__ == '__main__':
    app.run(debug=True)
