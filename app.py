from flask import Flask, render_template
app = Flask(__name__)

# What to display on the main page
@app.route('/')
def hello_world():
	author = "mer"
	name = "you"
	return render_template('index.html', author=author, name=name)



if __name__ == '__main__':
    app.run(debug=True)