from flask import Flask, render_template, request, session, redirect, url_for
import random
import string
import nltk

# Download dictionary and word meanings (WordNet)
try:
    nltk.data.find('corpora/words.zip')
    nltk.data.find('corpora/wordnet.zip')
except LookupError:
    nltk.download('words')
    nltk.download('wordnet')

from nltk.corpus import words, wordnet

app = Flask(__name__)
app.secret_key = 'hangman_secret_key_123'

# ASCII art stages for hangman
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

def get_random_word(level):
    """Return a random English word WITH a WordNet definition for correct hinting."""
    word_list = [w.lower() for w in words.words() if w.isalpha()]

    # Filter by level AND only choose words existing in WordNet
    if level == 'easy':
        filtered = [w for w in word_list if 4 <= len(w) <= 6 and wordnet.synsets(w)]
    elif level == 'medium':
        filtered = [w for w in word_list if 6 < len(w) <= 8 and wordnet.synsets(w)]
    else:
        filtered = [w for w in word_list if len(w) > 8 and wordnet.synsets(w)]

    word = random.choice(filtered)
    synsets = wordnet.synsets(word)

    # Always get best (most common) meaning
    synsets = sorted(synsets, key=lambda s: -s.lemmas()[0].count())
    best_synset = synsets[0]
    definition = best_synset.definition()
    pos = best_synset.pos()
    examples = best_synset.examples()
    example_text = f' Example: "{examples[0]}"' if examples else ''
    hint = f"{definition.capitalize()} (POS: {pos}){example_text}"

    return word, hint

@app.route('/')
def home():
    session.clear()
    return render_template('level.html')

@app.route('/set_level', methods=['POST'])
def set_level():
    level = request.form.get('level')
    word, hint = get_random_word(level)
    session['word'] = word
    session['hint'] = hint
    session['guesses'] = []
    session['turns'] = 6
    session['level'] = level
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    word = session.get('word')
    hint = session.get('hint', '')
    guesses = session.get('guesses', [])
    turns = session.get('turns', 6)
    level = session.get('level', 'easy')

    if not word:
        return redirect(url_for('home'))

    message = ''

    if request.method == 'POST':
        guess = request.form.get('guess', '').lower()

        if not guess or guess not in string.ascii_lowercase:
            message = "⚠️ Please enter a valid letter!"
        elif guess in guesses:
            message = f"🔁 You already guessed '{guess}'!"
        else:
            guesses.append(guess)
            session['guesses'] = guesses
            if guess not in word:
                turns -= 1
                session['turns'] = turns
                message = f"❌ '{guess}' is not in the word."

    display_word = ' '.join([ch if ch in guesses else '_' for ch in word])
    stage = HANGMAN_PICS[6 - turns]

    if '_' not in display_word:
        message = f'🎉 You Win! The word was "{word}".'
        session.clear()
    elif turns == 0:
        message = f'💀 You Lose! The word was "{word}".'
        session.clear()

    return render_template(
        'index.html',
        display_word=display_word,
        turns=turns,
        guesses=guesses,
        stage=stage,
        message=message,
        hint=hint,
        level=level
    )

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
