#! /usr/bin/python3

import sys
class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        pass
    
    def __enter__(self):
        try:
            self.file = open(self.filename, 'rt')
        except:
            print("No such file")
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getdata(self):
        self.file.seek(0)
        if self.header == True:
            lines = self.file.readlines(1)
        lines = self.file.readlines()
        return lines

    def getheader(self):
        self.file.seek(0)
        if self.header == True:
            return self.file.readline()
        else:
            return None




if __name__ == "__main__":
    with CsvReader('aa.csv') as file:
        if file == None:
            print("File is corrupted")

    with CsvReader('aa.csv', header=True) as file:
        data = file.getdata()
        header = file.getheader()

print("Header: "+ header)

print("Data : ", data)
