import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/index',methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('template.html')
	else:
		global url_to_shorten
		url_to_shorten = request.form['url']
		global shortened_url
		shortened_url = 'not doing this quite yet'
		
		return redirect('/result')
		
@app.route('/result')
def display_shortened_url():
	return render_template('result.html',long_url=url_to_shorten,short_url=shortened_url)
		
		
		
		
		
if __name__ == "__main__":
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)