#!/usr/bin/env python 
# -*- coding: utf-8 -*-

###############################################
#
# 统计产品代码中的全量函数、DT覆盖的函数数量和DTFuzz覆盖的函数
#
###############################################

import os
import sys

import counter

sys.path.append("../..")
from utils import JsonOp


if __name__ == "__main__":
    funcs_total = {}
    funcs_DT = {}
    funcs_fuzz = {}

    # 产品源代码路径和dt测试代码路径
    # src_dir = input("source dir:")
    # dt_dir = input("dt dir:")
    src_dir = '/root/workspace/cwork/Ctest2Fuzz/testcase'
    dt_dir = '/root/workspace/cwork/Ctest2Fuzz/testcase'
    if not (os.path.exists(src_dir) and os.path.exists(dt_dir)):
        print("Dir not exists. Exit.")
    src_scanner = counter.FileScanner(src_dir, counter.TYPESRC)
    dt_scanner = counter.FileScanner(dt_dir, counter.TYPETEST)

    with open("./include.txt", 'r') as f:
        includedirs = ["-I"+os.path.abspath(i.strip()) for i in f.readlines()]
    

    src_scanner.Scan(includedirs, total_file="./total")
    dt_scanner.Scan(includedirs, total_func=src_scanner.func_total)


    res = {
        "total": list(src_scanner.func_total),
        "dt": list(dt_scanner.func_dt),
        "fuzz": list(dt_scanner.func_fuzz   )
    }    
    JsonOp.dump(res, "./count_res/xx.json")