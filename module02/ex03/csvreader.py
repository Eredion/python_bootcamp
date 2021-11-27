#!/usr/bin/env python

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            if not self.file.closed:
                self.file.close()

    def getheader(self):
        if not self.header:
            return None
        return file.readline().strip().split(self.sep)

if __name__ == '__main__':

    file = open('test.csv', 'r')
    line = file.readline().strip().split(',')
    print(line)

