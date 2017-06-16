

import webapp2
import cgi
import os
import jinja2

template_dir=os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

form="""
<form>
<input type="text"></input>
</form>
"""

class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
         self.response.out.write(*a,**kw)
    def render_str(self,template,**params):
         t=jinja_env.get_template(template)
         return t.render(params)
    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))



class MainPage(Handler):
    def escape_html(self,s):
        return cgi.escape(s,quote=True)

    def get(self):
        self.render("shopping_list.html")

    def post(self):
        pass





app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
