#!/usr/bin/env python
'''
Created on 18.04.2018

@author: trevaz (tristan.revaz@epfl.ch)

---------------------------------------------------------------------------------
app: monitor2 (log)
---------------------------------------------------------------------------------
'''

#################################################################################
# IMPORTS
#################################################################################
import os
from fctlib import get_case_path

#################################################################################
# CONSTANTS
#################################################################################


#################################################################################
# MAIN FUNCTION
#################################################################################
def monitor2(PATH, case_name):
    '''
    DEF:    monitor2 case (log).
    INPUT:  - case_name: name of the case, type=string
    OUTPUT: - ()
    '''
    case_path = get_case_path(PATH, case_name)
    os.system('tail -f ' + str(os.path.join(case_path, 'log')))
