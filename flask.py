from flask import Flask
app = Flask(__name__)


@app.route('/')
def home_page():
    return 'This is ok'  


@app.route('/extra')
def extra():
    return '''
    <html>
        <body>
            <h3>Extra</h3>
        </body>
    <html>

    '''

    
if __name__ == '__main__':
    app.run(debug=True)