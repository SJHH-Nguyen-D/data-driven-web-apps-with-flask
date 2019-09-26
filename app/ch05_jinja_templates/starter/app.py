"""
VIEW METHODS are defined in the app.py script and they direct us to the appropriate html template windows (views).
Each view method typically is associated with directing us in the browser to the appropriate window, which is identified by a specific
pattern in the URL. Each route view method and route should have a corresponding HTML view page.

The typical naming convention for the corresponding HTML template views take on the name of the view method followed by the .html extension:

Example:

* View method:
	* index()
* HTML view page:
	* index.html

* View method:
	* gallery()
* HTML view page:
	* gallery.html
"""

import flask

app = flask.Flask(__name__)

def get_latest_packages():
	return [
		{"name": "flask", "version": "1.2.3"},
		{"name": "sqlalechemy", "version": "2.2.0"},
		{"name": "passlib", "version": "2.1.2"},
	]

# this view method is the 'Controller' portion of the MVC model (Model View Controller)
@app.route('/')
def index():
	""" this is the view method for the index or Home Page of our website """
	# notice how you don't have to specify './templates/index.html"
	# This is because flask automatically detects the html in the project locally, so you don't have to worry about specifying the relatve
	# directory
	test_packages = get_latest_packages()
	return flask.render_template("index.html", packages=test_packages) # The index.html is the view portion of the MVC model

@app.route('/about')
def about():
	""" this is the view method the About html template page """
	return flask.render_template("about.html") # The index.html is the view portion of the MVC model

if __name__ == "__main__":
	app.run()