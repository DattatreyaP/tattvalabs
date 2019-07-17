from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/ind')
def index():
    return render_template("web_page.html")

@app.route('/home')
def index11():
    return "<h1><center>  For developers, by developers </center> </h1>" \
           "<h3> Stack Overflow is an open community for anyone that codes. We help you get answers to your toughest coding questions, share knowledge with your coworkers in private, and find your next dream job.  </h3>"

@app.route('/aboutus')
def index22():
    return "<h1><center>For businesses, by developers</center></h1>" \
           "<h3>Our mission is to help developers write the script of the future. This means helping you find and hire skilled developers for your business and providing them the tools they need to share knowledge and work effectively.  </h3>"

@app.route('/contactus')
def index33():
    return render_template("contact.html")

@app.route('/feedback')
def index44():
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run()