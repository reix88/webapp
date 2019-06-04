from flask import Flask, render_template, request
from search4w import search4w

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
	word = request.form['word']
	letters = request.form['letters']
	title = 'Here are your results:'
	results = str(search4w(word, letters))
	print(results)
	return render_template( 'results.html',
							the_word=word,
							the_letters=letters,
							the_title=title,
							the_results=results)

@app.route('/')	
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html', the_title='Search Engine')

if __name__ == '__main__':
	app.run(debug=True)
