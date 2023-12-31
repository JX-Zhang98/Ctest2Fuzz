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
    '''
    # getTestFuncsFromFile 从一个文件root node 中分析全部的Test函数，并返回cursor的列表
    '''
    res = []
    for node in root.get_children():
        # print(node, node.kind, node.spelling)
        if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            if node.spelling.startswith("TEST"):
                print(Color.green(node.spelling))
                # yield node
                res.append(node)
    return res


def get_callee_from_func(node:clang.cindex.Cursor)->list[str]:
    '''
    # get_callee_from_func 获取一个函数中全部的callee，并返回callee函数名的字符串
    '''
    callees = []
    last_token = ''
    for token in node.get_tokens():
        value = token.spelling
        cursor = token.cursor
        print("name: {}, kind: {}".format(value, cursor.kind))
        if value == "(":
            callees.append(last_token)
        last_token = value

    
    return callees
    



# TODO: 将修改后的AST以合适的形式输出 
def saveCode(root:clang.cindex.Cursor, filename:str):
    modifiedCode = ""
    lastToken = None
    spelling = ""
    for token in root.get_tokens():
        spelling = token.spelling
        cursor = token.cursor
        # TODO: 支持多种类型
        # TODO: 自定义类型不认识会识别为CursorKind.DECL_STMT
        if cursor.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
            # if cursor.semantic_parent.kind == clang.cindex.CursorKind.VAR_DECL:
            if lastToken.spelling == "=":
                assign = cursor.semantic_parent
                value = cursor                
                valuetokens = [t for t in value.get_tokens()]
                print(Color.green("type: {}, name:{}, value:{}".format(assign.type.spelling, assign.displayname, valuetokens[0].spelling)))
                spelling = "SetGetInt({})".format(spelling)



        modifiedCode += spelling
        ## TODO here
        # if token.kind.name == "KEYWORD" or token.kind.name == "IDENTIFIER":
        #     modifiedCode += " "
        lastToken = token

    print(modifiedCode)
    with open(filename, 'w') as f:
        f.write(modifiedCode)