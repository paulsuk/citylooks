from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/lel')
def lel():
	return render_template('index2.html')
        
if __name__ == '__main__':
    app.run(port=int("80"))