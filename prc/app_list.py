#!/usr/bin/env python
'''
Created on 18.04.2018

@author: trevaz (tristan.revaz@epfl.ch)

---------------------------------------------------------------------------------
app: list
---------------------------------------------------------------------------------
'''

#################################################################################
# IMPORTS
#################################################################################
import os

#################################################################################
# CONSTANTS
#################################################################################


#################################################################################
# MAIN FUNCTION
#################################################################################
def list(PATH, case_name):
    '''
    DEF:    list case.
    INPUT:  - case_name: name of the case, type=string
    OUTPUT: - ()
    '''
    print('CASES:\n')
    os.system('ls ' + PATH['job'])
