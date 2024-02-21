from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Stores the file path, creates a list of words from the file, and
        prints the amount of words read from that file"""
        self.file_path = path

        file = open(self.file_path)
        self.word_list = self.make_list(file)

        file.close()

        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return f"<WordFinder: holds list of words found in the file at {self.path}>"

    def make_list(self, file):
        """Takes the file, splits the lines into a list and return said list"""
        return [line.strip() for line in file]

    def random(self):
        """Returns random word from the read-in list of words"""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: finds random words from a dictionary while filtering
    out comments and blank lines"""

#  def __init__(self, path):  # unnecessary
#     """Stores the file path, creates a list of words from the file filtered
#    to not include empty spaces or comments, then prints the amount of
#   words read"""
#      super().__init__(path)

    def __repr__(self):
        return f"""<SpecialWordFinder: holds list of words found in the file at
        {self.path} minus any empty lines or comment lines>"""

    def make_list(self, file):
        """Takes the file, splits the lines into a list not including empty
        lines or comment lines and returns that list"""
        return [line.strip() for line in file if line != "\n" and not line.startswith('#')]  # for line in parent's super().make_list
