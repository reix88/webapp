from flask import Flask, render_template, request, escape
from search4w import search4w

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
	with open('search.log', 'a') as log:
		print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
	word = request.form['word']
	letters = request.form['letters']
	title = 'Here are your results:'
	results = str(search4w(word, letters))
	log_request(request, results)
	return render_template( 'results.html',
							the_word=word,
							the_letters=letters,
							the_title=title,
							the_results=results)

@app.route('/')	
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html', the_title='Search Engine')

@app.route('/viewlog')
def view_log() -> 'html':
	contents = []
	with open('search.log') as log:
		for line in log:
			contents.append([])
			for item in line.split('|'):
				contents[-1].append(escape(item))
	titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
	return render_template( 'viewlog.html',
							the_title = 'View Log',
							the_row_titles=titles,
							the_data=contents)

if __name__ == '__main__':
	app.run(debug=True)
	
# Hello
