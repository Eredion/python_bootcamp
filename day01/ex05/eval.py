#! /usr/bin/env python3

def check_input(words, coefs):
       try:
           if isinstance(words, list) and isinstance(coefs, list) and len(words) == len(coefs):
               for word in words:
                   if not isinstance(word, str):
                       return -1
               for coeg in coefs:
                   if not isinstance(coeg, float):
                       return -1
               return 1
           else:
               return -1
       except:
           return -1

class Evaluator:
    def zip_evaluate(words, coefs):
        if check_input(words, coefs) == -1:
            return -1
        ret = 0
        zipper = zip(words, coefs)
        for elem in zipper:
            ret += len(elem[0]) * elem[1]
        return ret
    
    def enumerate_evaluate(words, coefs):
        if check_input(words, coefs) == -1:
            return -1
        ret = 0
        for i, j in enumerate(words):
            ret += len(j) * coefs[i]
        return ret          

words = ['Le', 'Lorem', 'Ipsum', 'est', 'simple']
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(words, coefs))

print(Evaluator.enumerate_evaluate(words, coefs))
