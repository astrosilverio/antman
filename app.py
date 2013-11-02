import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/index',methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('template.html')
	else:
		# request was a POST
		url_to_shorten = request.form['url']
		
if __name__ == "__main__":
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)