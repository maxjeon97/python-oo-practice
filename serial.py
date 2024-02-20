class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Creates a serial number generator that starts at a number, start"""
        self.start = start
        self.generated_num = start - 1

    def __repr__(self):
        return f"<Serial number generator that starts at {self.start}>"

    def generate(self):
        """Returns the next sequential number"""
        self.generated_num += 1
        return self.generated_num

    def reset(self):
        """Resets the number back to the original start number"""
        self.generated_num = self.start - 1


