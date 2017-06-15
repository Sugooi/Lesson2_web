

import webapp2
import cgi

form="""
<form method="post" >
<b><h1>Birth Details:</b></h1><br>
Year:<input name="Year" value="%(year)s">
Month<input name="Month" value="%(month)s">
Date<input name="Date" value="%(date)s">
<input type="submit">
<br>
<br>
<h2><div style="color:red">%(error)s</div></h2>
</form>
"""

class MainPage(webapp2.RequestHandler):
    def escape_html(self,s):
        return cgi.escape(s,quote=True)

    def write_form(self,error="",month="",date="",year=""):
        self.response.out.write(form%{"error":error,"month":self.escape_html(month),"date":self.escape_html(date),"year":self.escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_year=self.request.get("Year")
        user_month=self.request.get("Month")
        user_date=self.request.get("Date")

        year=self.valid_year(user_year)
        month=self.valid_month(user_month)
        date=self.valid_date(user_date)

        if year and month and date:
            self.redirect('/thanks')
        else:
            self.write_form("That doesnt look correct. :/",user_month,user_date,user_year)


    def valid_month(self,month):
        months={"January","Febuary","March","April","May","June","July","August","September","October","November","December"}
        month_abr=dict((m[:3].lower(),m) for m in months)
        if month:
            short_month=month[:3].lower()
            return month_abr.get(short_month)

    def valid_date(self,day):
        if day:
            if day.isdigit():
                day=int(day)
                if day>0 and day<31:
                    return day

    def valid_year(self,year):
        if year:
            if year.isdigit():
                year=int(year)
                if year>1800 and year<=2017:
                    return year
class ThankPage(webapp2.RequestHandler):
    """docstring fs ThankPage."""
    def get(self):
        self.response.out.write("Thank!, Thats a totally valid date :)")




app = webapp2.WSGIApplication([('/', MainPage),('/thanks',ThankPage)], debug=True)
