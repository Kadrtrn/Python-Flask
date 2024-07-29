import datetime
from flask import Flask, render_template, request
from mongoDB import db


app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def home():

	if request.method == 'POST':
		entry_content = request.form.get('content')
		formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')
		
		db.entries.insert_one({'content': entry_content, 'date': formatted_date})

	entries_with_date = [
		(
			entry['content'],
			entry['date'],
			datetime.datetime.strptime(entry['date'], '%Y-%m-%d').strftime('%b-%d')
		)
		for entry in db.entries.find({})
	]
	return render_template('home.html',entries = entries_with_date)





if __name__ == '__main__':

	app.run(host='0.0.0.0',port=5000,debug=True)
