# main.py
# the import section
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())  # the response

class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render())  # the response

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler)
], debug=True)
