#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import json
import clang.cindex

from utils import Color

def helloWorld(cnt:int)->list:
    res = []
    for i in range(cnt):
        res.append("xx")
    return res


def getFileAST(filename : str) :
    if not os.path.exists(filename):
        return None
    idx = clang.cindex.Index.create()
    codeUnit = idx.parse(filename)
    root = codeUnit.cursor
    return root


def traverseAndModify(root:clang.cindex.Cursor):
    print(root)
    TFNodes = getTestFuncsFromFile(root)
    
    for i in range(len(TFNodes)):
        TFnode = TFNodes[i]
        for child in TFnode.walk_preorder():
            print(f'{child.location}, {child.kind}, {child.spelling}')
            # TODO: 支持多种类型
            if child.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
                if child.semantic_parent.kind == clang.cindex.CursorKind.VAR_DECL:
                    assign = child.semantic_parent
                    value = child
                print(Color.green("type: {}, name:{}, value:...".format(assign.type.spelling, assign.displayname)))
                for t in value.get_tokens():
                    print(Color.yellow(t.spelling))
                    # t.spelling = "SetGetInt({})".format(t.spelling)
                


                
                # if nextNode.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
                #     print(Color.yellow("value: {}".format(9527)))
                pass

        pass
    

    pass




def getTestFuncsFromFile(root:clang.cindex.Cursor)->list[clang.cindex.Cursor]:
    res = []
    for node in root.get_children():
        # print(node, node.kind, node.spelling)
        if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            if node.spelling.startswith("TEST"):
                print(Color.green(node.spelling))
                # yield node
                res.append(node)
    return res

    



# TODO: 将修改后的AST以合适的形式输出 
def saveCode(root:clang.cindex.Cursor, filename:str):
    modifiedCode = ""
    for token in root.get_tokens():
        modifiedCode += token.spelling
        # if token.kind.name == "KEYWORD" or token.kind.name == "IDENTIFIER":
        #     modifiedCode += " "
    print(modifiedCode)
    with open(filename, 'w') as f:
        f.write(modifiedCode)