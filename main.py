
from flask import Flask, render_template, redirect, request
from flaskext.i18n import MultiLang

app = Flask(__name__)
app.config['LANGUAGES'] = ['en', 'nl', 'de']
app.config['SECRET_KEY'] = 'supersecret'
multi_lang = MultiLang(app)

flashcards = {
    'Fair dinkum': 'Echt waar',
    'She'll be right, mate': 'Komt goed, maat',
    'No worries': 'Geen probleem',
    'Chuck a shrimp on the barbie': 'Gooi een garnaal op de barbecue',
    'Piece of piss': 'Makkie',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translations = {}
    if request.method == 'POST':
        for saying, translation in flashcards.items():
            dutch_translation = request.form.get(saying)
            if dutch_translation:
                translations[saying] = dutch_translation
        return redirect('/results', translations)
    return render_template('index.html', flashcards=flashcards)

@app.route('/results')
def results():
    return render_template('results.html', translations=request.args)

if __name__ == '__main__':
    app.run()
