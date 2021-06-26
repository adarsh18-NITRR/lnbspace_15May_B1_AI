from flask import Flask, render_template, request
#redirect, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h3>This is home page<h3>'

@app.route('/enter')
def admin_page():
    return '''
    <html>
    <title>This is Flask5</title>
        <body>
            <h3>This is the Admin/Enter Webpage</h3>
            <a href='/login_form'><button>Login Page</button></a>
        </body>
    </html>
'''


@app.route('/login_form', methods=['GET','POST'])
def login_page():
    
    if request.method == 'GET':
        #with get requests we get a lot of things in form of dictionary
        print(request.args)
        
    elif request.method == 'POST' :
        #with post requests we get the form
        print(request.form)
    return render_template('login_form_post method.html')

###This is the html form format for reference
'''
      <form action="/">
        <div class="title">
          <i class="fas fa-pencil-alt"></i> 
          <h2>Register here</h2>
        </div>
        <div class="info">
          <input class="fname" type="text" name="name" placeholder="Full name">
          <input type="text" name="name" placeholder="Email">
          <input type="text" name="name" placeholder="Phone number">
          <input type="password" name="name" placeholder="Password">
          <select>
            <option value="course-type" selected>Course type*</option>
            <option value="short-courses">Short courses</option>
            <option value="featured-courses">Featured courses</option>
            <option value="undergraduate">Undergraduate</option>
            <option value="diploma">Diploma</option>
            <option value="certificate">Certificate</option>
            <option value="masters-degree">Masters degree</option>
            <option value="postgraduate">Postgraduate</option>
          </select>
        </div>
        <div class="checkbox">
          <input type="checkbox" name="checkbox"><span>I agree to the <a href="https://www.w3docs.com/privacy-policy">Privacy Poalicy for W3Docs.</a></span>
        </div>
        <button type="submit" href="/">Submit</button>
      </form>
'''

################################################################
if __name__=='__main__':
    app.run(debug=True, use_reloader=False)