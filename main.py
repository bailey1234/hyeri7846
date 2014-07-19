from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')
@app.route('/idea1')
def idea1():
    """Return a friendly HTTP greeting."""
    return render_template('index4.html')
@app.route('/idea2')
def idea2():
    """Return a friendly HTTP greeting."""
    return render_template('index5.html')
@app.route('/useit')
def useit():
    """Return a friendly HTTP greeting."""
    return render_template('useit.html')          


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
