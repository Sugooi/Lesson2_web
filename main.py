import webapp2
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
Password_RE=re.compile(r"^.{3,20}$")
Email_RE= re.compile(r"^[\S]+@[\S]+.[\S]+$")

form="""
<form method="post">
<h1><b>Sign up</h1></b><br>
<table >
<tr>
<td class="label">Username:</td>
<th><input type="text" name="username" value="%(user_name)s"></input></th>
<td style="color:red">%(error_name)s</td>
</tr>
<tr>
<td>Password:</td>
<th>
<input type="password" name="password" value="" ></input></th>
<td style="color:red">%(error_pass)s</td>
</tr>
<tr>
<td>Verify Password:</td>
<th>
<input type="password" name="verify" value="" ></input></th>
<td style="color:red">%(error_verify)s</td>
</tr>
<tr>

<td>Email:</td>
<th>
<input type="text" name="email" value="%(user_mail)s"></input></th>
<td style="color:red">%(error_email)s</td>
</tr>
</table>
<input type="submit"></input>
</form>

"""
class MainPage(webapp2.RequestHandler):
	def valid_username(self,username):
		return USER_RE.match(username)
	def valid_password(self,password):
		return Password_RE.match(password)
	def valid_email(self,email):
		return Email_RE.match(email)

	def write_form(self,error_name="",error_pass="",error_verify="",error_email="",user_name="",user_mail=""):
		self.response.out.write(form%{"error_name":error_name,"error_pass":error_pass,"error_verify":error_verify,"error_email":error_email,"user_name":user_name,"user_mail":user_mail})

	def get(self):
		self.write_form()
	def post(self):
		user_name=self.request.get("username")
		user_pass=self.request.get("password")
		user_mail=self.request.get("email")
		user_verify=self.request.get("verify")

		valid_name=self.valid_username(user_name)
		valid_pass=self.valid_password(user_pass)
		valid_email=self.valid_email(user_mail)

	 	if not valid_name:
			error_name="Invalid Username!"
		else:
			error_name=""
		if not valid_pass:
			error_pass="Invalid Password"
		else:
			error_pass=""
		if not valid_email:
			error_email="Invalid Email!"
		else:
			error_email=""
		if not (user_pass==user_verify):
			error_verify="Password not same!"
		else:
			error_verify=""


		self.write_form(error_name,error_pass,error_verify,error_email,user_name,user_mail)

		if valid_name and valid_email and valid_pass and (user_pass==user_verify):
			self.redirect("/welcome")

class Welcome(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thank You for regestering!")


app = webapp2.WSGIApplication([
('/', MainPage),('/welcome',Welcome)
], debug=True)