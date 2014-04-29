#!/usr/bin/env python

import sys
import os

##############  Initial path adding to system search path ###################
init_path  = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0,init_path)