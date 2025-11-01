# 🪓 Hangman Game  
_A Modern Web Hangman with Flask & NLTK_

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)](https://flask.palletsprojects.com/)
[![NLTK](https://img.shields.io/badge/NLTK-WordNet-orange?logo=python)](https://www.nltk.org/)

---

A playful and educational *Hangman* game built with [Flask](https://flask.palletsprojects.com/) (Python) and [NLTK WordNet](https://www.nltk.org/howto/wordnet.html).  
Pick your difficulty, guess the word, and get instant dictionary hints and examples!  
Perfect for boosting vocabulary and having fun. 🚀

---

## ✨ Features

- **Three levels:** Easy / Medium / Hard
- **Real dictionary hints:** Meaning + part of speech + example from WordNet
- **Hangman ASCII art:** Classic graphics
- **Session-based logic:** Secure, multi-game play
- **Replay:** One-click replay
- **Sleek UI:** Modern and minimal web design

---

## 🚀 Live Demo

<table>
  <tr>
    <th>Easy Mode</th>
    <th>Example Hint</th>
    <th>Victory</th>
    <th>Wrong Guesses</th>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/<yourusername>/<yourrepo>/main/screenshots/Screenshot-2025-11-01-171411.jpg" alt="Easy Mode" width="320"></td>
    <td><img src="https://raw.githubusercontent.com/<yourusername>/<yourrepo>/main/screenshots/Screenshot-2025-11-01-171447.jpg" alt="Example Hint" width="320"></td>
    <td><img src="https://raw.githubusercontent.com/<yourusername>/<yourrepo>/main/screenshots/Screenshot-2025-11-01-171603.jpg" alt="Victory" width="320"></td>
    <td><img src="https://raw.githubusercontent.com/<yourusername>/<yourrepo>/main/screenshots/Screenshot-2025-11-01-171717.jpg" alt="Wrong Guesses" width="320"></td>
  </tr>
</table>

---

## 🏁 Getting Started

Clone and run locally:

git clone https://github.com/Priyanshu-2005-18/hangman-flask-nltk.git
cd hangman-flask-nltk
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install flask nltk
python app.py


Open [localhost:5000](http://127.0.0.1:5000/) in your browser!

---

## 📦 Project Structure

hangman-flask-nltk/
│
├── app.py # Main Flask app
├── templates/
│ ├── index.html # Game screen
│ └── level.html # Level selection
├── static/ # Optional: styles/images
└── README.md # This file
undefined

---

## 🛠️ Customization

- 🎯 **Word Source:** Use school word lists or your own corpus.
- 🎨 **Themes:** Tweak styles, ASCII art, or replace with SVG.
- 💡 **Hints:** Edit logic in `get_random_word` for custom clues/synonyms.
- ☁️ **Deploy:** Heroku / PythonAnywhere / Render support.

---

## 🤝 Contributing

Pull requests, issues and suggestions are welcome!
Check out the [issues](https://github.com/yourusername/hangman-flask-nltk/issues) tab to get started.

---

## 📄 License

MIT License — Free to use and extend!

---

## 👤 Author & Contact

Made with ❤️ by Priyanshu-2005-18 
Questions? Connect via [GitHub Issues](https://github.com/Priyanshu-2005-18/hangman-flask-nltk/issues) 
