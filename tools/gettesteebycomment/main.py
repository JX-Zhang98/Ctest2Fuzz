#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 

import os
import sys

def get_c_files(dirname):
        files = []        
        for entry in os.listdir(dirname):
            path = os.path.join(dirname, entry)
            if os.path.isfile(path) and path.endswith(".c") or path.endswith(".cpp"):
                files.append(path)
            elif os.path.isdir(path):
                files += get_c_files(path)
        return files

def get_testee(cf)->set:
    testee = set()
    with open(cf, 'r') as f:
        lines = [i.strip() for i in f.readlines() if i.strip()]
    for l in lines:
        if "用例名称" not in l:
            continue
        try:
            testee_name = l.split("test_")[1].rsplit("_", 1)[0]
            testee.add(testee_name)
        except:
            print("[-] testname parse failed")
    return testee
    


if __name__ == "__main__":
    all_testees = set()
    # 模块llt的目录
    testdir = "" 
    assert(os.path.exists(testdir))
    # 全部test文件
    c_files = get_c_files(testdir)

    for cf in c_files:
        testee = get_testee(cf)
        all_testees.update(testee)
    with open("./testees.txt", 'a') as f:
        f.writelines([tname for tname in testee])
    

