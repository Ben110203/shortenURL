import flask

app = flask.Flask(__name__)

URLdict = {"abc":"www.google.com.tw"}

@app.route("/<path>")
def reponse(path):
    return  flask.redirect(getURL(path))

def getURL(url):
    if URLdict.get(url,None)!= None:
        return URLdict[url]
    else:
        return None


if __name__ == "__main__":
    app.run()