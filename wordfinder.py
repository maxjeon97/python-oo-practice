class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Stores the file path"""
        self.file_path = path
        self.word_list = self.make_list()
        print(f"{len(self.word_list)} words read")

    def make_list(self):
        """Opens the file, splits the lines into a list and return said list"""
        file = open(self.file_path)
        word_list = file.splitlines()
        file.close()
        return word_list




