# Wiktionary-Based Language Detection of Words in Python
This repository contains the python code for a very basic Wiktionary lookup of terms to determine their language.

![license](https://img.shields.io/github/license/martinpauleve/detect-language) ![activity](https://img.shields.io/github/last-commit/MartinPaulEve/detect-language) 

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Install
    git clone git@github.com:MartinPaulEve/detect-language.git
    cd detect-language
    pip3 install -r ./requirements.txt


# Usage
    Usage: python -m detect_language [OPTIONS] COMMAND [ARGS]...
    
      Detect whether a word is a particular language
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      classify-word
      classify-words

To classify a word:

    python3 -m detect_language classify-word  --word="hello" --language="English"
    python3 -m detect_language classify-word  --word="hwaet" --language="Old English"

To classify a list of words in a file (we tokenize the words by comma, space, newline etc.):

    python3 -m detect_language classify-words --word-file=/home/martin/test.txt --language=latin

# Demo
[![asciicast](https://asciinema.org/a/LNdUrCjvAFeRkZ1X9lCKsEteX.svg)](https://asciinema.org/a/LNdUrCjvAFeRkZ1X9lCKsEteX)

# Credits
* [Click](https://click.palletsprojects.com/en/8.0.x/) for CLI argument parsing.
* [Git](https://git-scm.com/) from Linus Torvalds _et al_.
* [.gitignore](https://github.com/github/gitignore) from Github.
* [Requests](https://docs.python-requests.org/en/latest/) for remote fetch.
* [Rich](https://github.com/Textualize/rich) for beautiful output.
* [Wiktionary](https://en.wiktionary.org/).
* [Wiktionary Parser](https://github.com/Suyash458/WiktionaryParser) by Suyash458.

&copy; 2022 Martin Paul Eve