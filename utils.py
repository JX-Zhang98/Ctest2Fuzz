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