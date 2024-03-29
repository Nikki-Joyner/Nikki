import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# other functions should go above the handlers or in a separate file
def get_meme_url(meme_choice):
    if meme_choice == 'old-class':
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    elif meme_choice == 'college-grad':
        url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    elif meme_choice == 'thinking-ape':
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    elif meme_choice == 'coding':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
    return url


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        a_variable_dict = {"greeting": "Howdy",
                           "adjective": "amazing"}
        self.response.write(welcome_template.render(a_variable_dict))

class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        the_variable_dict = {
            "line1": "If Cinderella's shoe was a perfect fit",
            "line2": "Why did it fall off?",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
        }
        self.response.write(results_template.render(the_variable_dict))

    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        meme_img_choice = self.request.get('meme-type')

        pic_url = get_meme_url(meme_img_choice)
        the_variable_dict = {"line1": meme_first_line,
                             "line2": meme_second_line,
                             "img_url": pic_url}
        self.response.write(results_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler)
], debug=True)
