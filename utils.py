#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import json
import os
import sys

class Color:
    def red(s)->str:
        return "\033[31m{}\033[0m".format(s)
    def green(s)->str:
        return "\033[32m{}\033[0m".format(s)
    def yellow(s)->str:
        return "\033[33m{}\033[0m".format(s)


class JsonOp:
    def load(filename:str):
        with open(filename, 'r') as f:
            obj = json.load(f)
        return obj
    
    def dump(data, filename:str):
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return