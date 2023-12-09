#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os
import sys
import clang.cindex

sys.path.append("../..")
import myparser
from utils import Color

TYPESRC = "src"
TYPETEST="test"

class FileScanner:
    def __init__(self, dirname, type):
        self.root_dir = dirname
        self.type = type
        self.func_total = []
        self.func_dt = set()
        self.func_fuzz = set()
    
    def Scan(self, include_dir:list[str], total_file = None, total_func = None):
        cfiles = self.get_c_files(self.root_dir)
        for cf in cfiles:
            if self.type == TYPESRC:
                # 如果是src，分析全部定义的函数，并加入total
                # 如果total_file提供，直接从配置文件读取
                if total_file is not None and os.path.exists(total_file):
                    with open(total_file, 'r') as f:
                        self.func_total = [i.strip() for i in f.readlines()]
                        break
                else:
                    self.operator = ASTOperator(cf, include_dir)
                    self.func_total = self.operator.get_func_def()
                
            elif self.type == TYPETEST:
                # 如果是test，则分析其中全部函数的callee，并在total中进行匹配，
                # 同时检测是否存在SETGET调用，判定是否是fuzz
                self.operator = ASTOperator(cf, include_dir)
                func_dt, func_fuzz = self.operator.get_Test_covered(total_func)
                self.func_dt.update(func_dt)
                self.func_fuzz.update(func_fuzz)

            else:
                print("Invalid type!") 
    

    def get_c_files(self, dirname):
        files = []        
        for entry in os.listdir(dirname):
            path = os.path.join(dirname, entry)
            if os.path.isfile(path) and path.endswith(".c") or path.endswith(".cpp"):
                files.append(path)
            elif os.path.isdir(path):
                files += self.get_c_files(path)
        return files






class ASTOperator:
    def __init__(self, filename:str, include:list):
        idx = clang.cindex.Index.create()
        self.root = idx.parse(filename, args=include).cursor
    
    def get_func_def(self)->list[str]:
        # 疑似可以通过编译过程直接获取，先不实现
        pass

    def get_Test_covered(self, func_total:list[str])->(set, set):
        print(self.root)
        func_dt = set()
        func_fuzz = set()
        TF_nodes = myparser.getTestFuncsFromFile(self.root)
        for t in TF_nodes:
            callee_from_TF = myparser.get_callee_from_func(t)
            print(Color.yellow(callee_from_TF))
            is_fuzz = False
            target_func = ''
            for callee in callee_from_TF:
                if "setget" in callee.lower():
                    is_fuzz = True
                if callee in func_total:
                    target_func = callee
                if is_fuzz and target_func != "":
                    break

            if target_func == "":
                print(Color.red("target func not found in Test {}".format(t.spelling)))
                continue

            func_dt.add(target_func)
            if is_fuzz:
                func_fuzz.add(target_func)

        
        return (func_dt, func_fuzz)

    