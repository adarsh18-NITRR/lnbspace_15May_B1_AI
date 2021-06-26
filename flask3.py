from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'This is home page'

@app.route('/enter')
def admin_page():
    return f'''
    <html>
    <title>This is Flask</title>
        <body>
            <h3>This is the Admin webpage</h3>
        </body>
    </html>
'''

@app.route('/enter/<val>')
def guest_page(val):
    return f'''
    <html>
    <body>
        <h3>This is the enter webpage</h3>
        <p>Hello {val} </p>
    </body>
    </html>
'''

@app.route('/login/<name>')
def redirecter(name):
    if name =='admin':
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('guest_page', val=name))


if __name__=='__main__':
    app.run(debug=True, use_reloader=False)