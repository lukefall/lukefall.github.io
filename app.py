from flask import *
from whitenoise import WhiteNoise
app = Flask(__name__, template_folder="./")
app.wsgi_app = WhiteNoise(app.wsgi_app,
                          root='static/',
                          prefix='static/',
                          index_file='index.htm',
                          autorefresh=True)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
