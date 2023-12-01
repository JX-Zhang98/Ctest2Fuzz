#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys
import os


import myparser
import utils

if __name__ == "__main__":
	print(myparser.helloWorld(2))
	if len(sys.argv) <= 1:
		print("No file is given\nExisting...")
		exit(0)
	root = myparser.getFileAST(sys.argv[1])
	myparser.traverseAndModify(root=root)

	myparser.saveCode(root=root, filename="testcase/1.cpp.new")


