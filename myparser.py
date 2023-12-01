#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import json
import clang.cindex

def helloWorld(cnt:int)->list:
    res = []
    for i in range(cnt):
        res.append("xx")
    return res


def getFileAST(filename : str) :
    idx = clang.cindex.Index.create()
    codeUnit = idx.parse(filename)
    root = codeUnit.cursor
    return root


def traverseAndModify(root:clang.cindex.Cursor):
    print(root)
    
    
    pass


def saveCode(root:clang.cindex.Cursor, filename:str):
    modifiedCode = ""
    for token in root.get_tokens():
        modifiedCode += token.spelling
        # if token.kind.name == "KEYWORD" or token.kind.name == "IDENTIFIER":
        #     modifiedCode += " "
    print(modifiedCode)
    with open(filename, 'w') as f:
        f.write(modifiedCode)