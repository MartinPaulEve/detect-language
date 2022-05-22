import logging
import pathlib
import re

import click
from rich import pretty
from rich.logging import RichHandler

from WiktionaryParser import core as wik

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


@click.group()
def cli():
    """
    Detect whether a word is a particular language
    """
    pass


@click.command()
@click.option('--word',
              prompt='Word',
              help='The word to check')
@click.option('--language',
              prompt='Language',
              help='The language to check')
def classify_word(word, language):
    parser = wik.WiktionaryParser()
    log = logging.getLogger("rich")

    log.info('{} is {}: {}'.format(word,
                                   language.title(),
                                   _lookup_word(language, parser, word)))


def _lookup_word(language, parser, word):
    lookup = parser.fetch(word, language)
    is_lang = len(lookup) > 0 and len(lookup[0]['definitions']) > 0
    return is_lang


@click.command()
@click.option('--word-file',
              prompt='Word file',
              help='The word file to use (comma or space or newline separated)')
@click.option('--language',
              prompt='Language',
              help='The language to check')
def classify_words(word_file, language):
    parser = wik.WiktionaryParser()
    log = logging.getLogger("rich")

    file = pathlib.Path(word_file)

    try:
        with file.open('r') as in_file:
            words = in_file.read()

            # split the words by boundary (could use a different tokenizer as
            # required
            words = set(re.split(r'\W+', words))

            for word in words:
                log.info('{} is {}: {}'.format(word,
                                               language.title(),
                                               _lookup_word(language, parser,
                                                            word)))

    except (FileNotFoundError, IOError):
        log.error('Could not open {}'.format(file))
        return

    lookup = parser.fetch(word, language)

    is_lang = len(lookup) > 0 and len(lookup[0]['definitions']) > 0
    log.info('{} is Latin: {}'.format(word, is_lang))


if __name__ == '__main__':
    pretty.install()
    cli.add_command(classify_word)
    cli.add_command(classify_words)
    cli()
