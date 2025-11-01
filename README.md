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

**Mode**

![Easy Mode](https://github.com/Priyanshu-2005-18/Hangman_Solver/raw/main/Screenshot/Screenshot%202025-11-01%20171411.png)

**Example**

![Example Hint](https://github.com/Priyanshu-2005-18/Hangman_Solver/raw/main/Screenshot/Screenshot%202025-11-01%20171447.png)

**Victory**

![Victory](https://github.com/Priyanshu-2005-18/Hangman_Solver/raw/main/Screenshot/Screenshot%202025-11-01%20171603.png)

**Wrong Guesses**

![Wrong Guesses](https://github.com/Priyanshu-2005-18/Hangman_Solver/raw/main/Screenshot/Screenshot%202025-11-01%20171717.png)




---

## 🏁 Getting Started

### 1. Clone the Repository

git clone https://github.com/Priyanshu-2005-18/Hangman_Solver.git

cd Hangman_Solver

### 2. (Optional) Create and Activate a Virtual Environment

python -m venv venv

On Windows:

venv\Scripts\activate

On Linux/Mac:

source venv/bin/activate

### 3. Install Required Packages

pip install flask nltk


### 4. Download NLTK Data (if not done automatically):

import nltk

nltk.download('words')

nltk.download('wordnet')

You can run these commands in a Python shell (`python`) or IPython.

### 5. Run the Application

python app.py


### 6. Open Your Browser

Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to play the game!

---


## 📦 Project Structure

```
hangman-flask-nltk/
├── app.py             # Main Flask app
├── templates/
│   ├── index.html     # Game screen
│   └── level.html     # Level selection
├── static/            # Optional: styles/images
├── Screenshot/        # Demo screenshots for README
└── README.md          # This file
```
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
