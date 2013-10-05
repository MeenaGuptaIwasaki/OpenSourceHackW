#Code from open source hack workshop
#Modified By Meena Gupta-Iwasaki
#To do stuff


from OC import OC
import unittest

#acquire the articles from OC
articles = OC.articles.list()

#a function to print a return elements under '32 in a dictionary
def print32(articles):
    print articles['32']    #print the values under '32' in a dictionary
    return articles['32']; #return the values under '32' in a dictionary

#Attempt to test the function, but broken right now.
def testprint32(articles):
    unittest.assert(print32(articles) == articles['32'])

print32(articles)
