# Hangman Game (Flask & NLTK)

A web-based Hangman game built using Flask in Python. The game selects random English words at three difficulty levels and provides *meaningful dictionary hints* using NLTK’s WordNet. Beautiful, interactive interface and smooth gameplay make this a cool app for learning and fun!

## Features

- **Difficulty selection:** Easy / Medium / Hard (based on word length)
- **Word hints:** Shows real-time dictionary meaning, part of speech, and examples using WordNet
- **Hangman stages:** ASCII art graphics update with every wrong guess
- **Session management:** Game state is kept secure, multiple games can be played
- **Replay:** Quick replay after each game
- **Responsive web UI:** Simple, modern interface with clear messages

## Demo


<img width="1920" height="1080" alt="Screenshot 2025-11-01 171411" src="https://github.com/user-attachments/assets/7a56556a-ef6c-4d90-8fa6-cd99d40565f6" />

<img width="1920" height="1080" alt="Screenshot 2025-11-01 171447" src="https://github.com/user-attachments/assets/61dcaa74-6a1a-415b-b511-32b92ffceb78" />

<img width="1920" height="1080" alt="Screenshot 2025-11-01 171603" src="https://github.com/user-attachments/assets/930bea0e-8281-4429-bab8-f5427b04cbf7" />

<img width="1920" height="1080" alt="Screenshot 2025-11-01 171717" src="https://github.com/user-attachments/assets/51888da1-cc6c-4bb0-853e-8292a12cf7be" />



## Installation

1. **Clone the repository**

git clone https://github.com/yourusername/hangman-flask-nltk.git
cd hangman-flask-nltk

2. **Set up your environment**

You may want to use a Python virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. **Install requirements**

pip install flask nltk


4. **Download NLTK Data**

The app downloads required corpora (words, wordnet) automatically at first run.  
If you want to ensure it manually, run:

import nltk
nltk.download('words')
nltk.download('wordnet')

## Usage

1. **Run the application**

python app.py

2. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. Choose difficulty and start playing!

## Project Structure

hangman-flask-nltk/
│
├── app.py # Main Flask application
├── templates/
│ ├── level.html # Difficulty selection
│ └── index.html # Game screen
├── static/ # (optional: custom styles, images)
└── README.md # Project documentation


## Customization

- **Word Sources**: You may filter words for specific grade/class levels or use your own corpus.
- **Themes**: Customize styles, add animations in `index.html`, or create your own ASCII drawing!
- **Hints**: Change the way hints are generated in `get_random_word` to show synonyms, advanced clues or exclude obscure meanings.
- **Deployment**: Host on services like Heroku, PythonAnywhere, Render, etc.

## License

MIT License.  
Feel free to use, share, or extend this project!

## Credits

- Built with [Flask](https://flask.palletsprojects.com/)
- Word meanings powered by [NLTK WordNet](https://www.nltk.org/howto/wordnet.html)
