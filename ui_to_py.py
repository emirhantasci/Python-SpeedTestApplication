# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:34:21 2022

@author: emirh
"""

from PyQt5 import uic

with open('SpeedTestWindow.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('SpeedTestWindow.ui', fout)