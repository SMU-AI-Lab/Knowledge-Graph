import sys 
import pandas as pd
import numpy as np
import json
from chemdataextractor import Document
from glob import glob
import re

outFile = open('tree.txt', 'w') 
mainRoot = None;
class Node:
    def __init__(self, data, title):

        self.left = None
        self.right = None
        self.data = data
        self.title = title
        self.root = None

# Insert method to create nodes
    def insertInto(self,data, title):
    	if self.root is None:
    		self.root = root
    		mainRoot = root
    	else:
	        if self.title:
	            if title < self.title:
	                if self.left is None:
	                    self.left = Node(data,title)
	                else:
	                    self.left.insertInto(data,title)
	            elif title > self.title:
	                if self.right is None:
	                    self.right = Node(data,title)
	                else:
	                    self.right.insertInto(data,title)
	        else:
	            self.title = title
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.title:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.title:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.title) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.title),
        if self.right:
            self.right.PrintTree()

    def PPF():
    	printPreorderFile(mainRoot) 

    def printPreorderFile(root):
        outFile = open('tree.txt', 'a') 
        # First print the data of node
        print(root.title, " - ", root.data, file = outFile)
        #print(root.title, " - ", root.data)
  
        # Then recur on left child 
        if (root.left is not None) :
            root.left.printPreorderFile() 
  
        # Finally recur on right child 
        if (root.right is not None) :
            root.right.printPreorderFile() 

#-----------------------------------------------------------------------------------------------------------------

data_dir = 'D:/Downloads/cord19/document_parses/pdf_json'
files = glob(data_dir + '/*.json')
numFiles = len(files)
fileNum = 640
print("Starting") 
try:
    outFile = open('pureIndex.txt', 'a') 
except IOError:
    print ("Could not open file!")
root = None 
numSEFiles = 0

#------------------------------------------

while fileNum < numFiles:
    with open(files[fileNum]) as f:
        data = json.load(f)
#------------------------------------------
    body = ""

    for p in data["body_text"]:
        body += p["text"] + ' \n'
    
    bod = Document(body)
    bod.records.serialize()
    x=None
#------------------------------------------
    for i in data['abstract']: 
        abst = i['text']
        #print(abst) 
    x = re.search("subjects |effects |effect |side", abst)
    tit = data['metadata']['title']
#------------------------------------------
    if root is None and x:
        print(x)
        root = Node(x,tit)
        numSEFiles +=1
        #print(":",numSEFiles)
        if tit == "" or tit == '' or tit == " " or tit == ' ':
            tit = data['paper_id']
            #print("fixed title ",fileNum+1) 
        try:
            print(tit, " - ", x, file = outFile)
        except:
            print("fixed file ",fileNum+1) 
            tit = data['paper_id']
            print(tit, " - ", x, file = outFile)
    elif x :
        numSEFiles +=1
        #print(":",numSEFiles)
        if tit == "" or tit == '' or tit == " " or tit == ' ':
            tit = data['paper_id']
            #print("fixed title ",fileNum+1) 
        try:
            print(tit, " - ", x, file = outFile)
        except:
            print("fixed file ",fileNum+1) 
            tit = data['paper_id']
            print(tit, " - ", x, file = outFile)

    if (fileNum+1)%100 ==0: 
        print(fileNum+1 , "/" , numFiles) 

    fileNum+=1

#root.printPreorderFile() 

print("Complete") 