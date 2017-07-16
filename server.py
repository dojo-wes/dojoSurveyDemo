from flask import Flask, render_template, request, flash, session, redirect
app = Flask(__name__)

app.secret_key = "SuperSecretKey!"

@app.route('/')
def index():
	return render_template('index.html', title="Dojo Survey Home")

@app.route('/result', methods=['POST'])
def result():
	# Print information to check if server is receiving data correctly
	# print "*" * 80
	# print request.form['user_name']
	# print "*" * 80
	# back_end_user_name = request.form['user_name']


	# run validations 1
	# if(len(request.form['user_name']) < 2):
	# 	print "name validation failed"
	# 	flash("You must enter a name that is at least 2 characters long!")
	# 	return redirect('/')

	# if(len(request.form['comment']) > 120):
	# 	print "comment validation failed"
	# 	flash("Comment must be under 120 characters long")
	# 	return redirect('/')

	#	run validations 2
	error_messages = []

	if(len(request.form['user_name']) < 2):
		print "*" * 80
		print "name validation failed"
		print "*" * 80
		error_messages.append("You must enter a name that is at least 2 characters long!")

	if(len(request.form['comment']) > 120):
		print "*" * 80
		print "comment validation failed"
		print "*" * 80
		error_messages.append("Comment must be under 120 characters long!")

	print error_messages
	if(error_messages):
		for error in error_messages:
			flash(error)
		return redirect('/')

	# Create a dictionary to store data
	results = {}

	# print request.form.items()

	# Loop through the form elements and save key value pairs in results dict
	for key, value in request.form.items():
		results[key] = value

	# print results
	return render_template('result.html', title="Results!", results=results)

app.run(debug=True)