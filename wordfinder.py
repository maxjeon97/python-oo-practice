from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> word_finder = WordFinder(path="words.txt")
    20 words read

    >>> word_finder.make_list(open("words.txt"))
    ['lion', 'monkey', 'cat', 'dog', 'porcupine', 'elephant', 'giraffe', 'pigeon', 'tiger', 'cheetah', 'gorilla', 'panda', 'rat', 'dolphin', 'whale', 'shark', 'walrus', 'penguin', 'seal', 'otter']

    >>> word_finder.random() in word_finder.word_list
    True

    >>> word_finder.random() not in word_finder.word_list
    False

    >>> isinstance(word_finder.random(), str)
    True

    >>> isinstance(word_finder.random(), int)
    False
    """

    def __init__(self, path):
        """Stores the file path, creates a list of words from the file, and
        prints the amount of words read from that file"""
        file = open(path)
        self.word_list = self.make_list(file)

        file.close()

        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return f"""<{type(self).__name__} contains list of {len(self.word_list)} words>"""

    def make_list(self, file):
        """Takes the file, splits the lines into a list and return said list"""
        return [line.strip() for line in file]

    def random(self):
        """Returns random word from the read-in list of words"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: finds random words from a dictionary while filtering
    out comments and blank lines

    >>> special_word_finder = SpecialWordFinder(path="special_words.txt")
    24 words read

    >>> special_word_finder.make_list(open("special_words.txt"))
    ['lion', 'monkey', 'cat', 'dog', 'porcupine', 'elephant', 'giraffe', 'pigeon', 'tiger', 'cheetah', 'gorilla', 'panda', 'rat', 'dolphin', 'whale', 'shark', 'walrus', 'penguin', 'seal', 'otter', 'termite', 'ant', 'bee', 'donkey']

    >>> special_word_finder.random() in special_word_finder.word_list
    True

    >>> special_word_finder.random() not in special_word_finder.word_list
    False

    >>> isinstance(special_word_finder.random(), str)
    True

    >>> isinstance(special_word_finder.random(), int)
    False

    """

    def __repr__(self):
        return super().__repr__()[:-1] + " without empty spaces and comments>"

    def make_list(self, file):
        """Takes the file, splits the lines into a list not including empty
        lines or comment lines and returns that list"""
        return [line for line in super().make_list(file) if line != "" and not
                line.startswith('#')]
