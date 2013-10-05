Copyright 2013 Meena Gupta-Iwasaki

Licensed under the Apache License, Version 2. (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/License-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language govering permissions and
  limitations under the License.



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
