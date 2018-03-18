import flask

app = flask.Flask(__name__)

URLdict = {"abc":"www.google.com.tw"}

@app.route("/<path>")
def reponse(path):
    return  flask.redirect(getURL(path))

def getURL(url)

    try:

        if URLdict.get(url,None)!= None:
            return flask.redirect(URLdict[url])
        else:
            return None
    except:
        return "ERROR"

if __name__ == "__main__":
    app.run()
