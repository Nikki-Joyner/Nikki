#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import random


def get_fortune():
    fortune_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(fortune_list))


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/fortune_start.html")
        self.response.write(start_template.render())

    def post(self):
        random_fortune = get_fortune()
        user_astrological_sign = self.request.get("user_astrological_sign")
        my_dict={
        'the_fortune': random_fortune,
        'the_user_astrological_sign':user_astrological_sign
        }
        end_template=jinja_current_directory.get_template("templates/fortune_results.html")
        self.response.write(end_template.render(my_dict))


class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of Fortune Teller')

# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler) #maps '/predict' to the FortuneHandler
], debug=True)
