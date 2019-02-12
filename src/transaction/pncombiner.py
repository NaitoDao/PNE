# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 20:43:04 2019

@author: LiNaK
"""

# Standard module

# 3rd party's module

# Original module  

#interfaces
from src.interface.intfc_com import Transaction
#from src.interface.calc_data import (PN_TF_Calc)

#utilities
from src.utility.utility import singleton_decorator, read_only_getter_decorator
from src.dataio.csvio import CSVIO


class PNCombiner(Transaction):
    def __init__(self):
        self._reader = PNDataReader()
        self._writer = PNDataWriter()
        self._pnc = PNCalc()
    
    def execute(self):
        pass

class PNDataReader(Transaction):
    def __init__(self):
        self.csvio = CSVIO()
        self.pnpm = PNPrmtrMng()
        self.pndb = PNDataBase()
        self._make_msg()
    
    def _make_msg(self):
        self._msg ={self.pnpm.ref:"Please input reference phase noise."}
    
    def execute(self):
        data = self.csvio.read(self._msg[self.pnpm.ref])
        self.pndb.set_noise(self.pnpm.ref, data)

class PNDataWriter(Transaction):
    def execute(self):
        pass

class PNCalc(Transaction):
    def execute(self):
        pass

@singleton_decorator
class PNDataBase():
    def __init__(self):
        self._noise = {}
    
    def set_noise(self, name, data):
        self._noise[name] = data
    
    def get_noise(self, name):
        return self._noise[name]
    
    def set_transfer_func(self):
        pass
    
    def get_transfer_func(self):
        pass
    
    def set_pn(self):
        pass
    
    def get_pn(self):
        pass


@read_only_getter_decorator({'ref':'reference', 'vco':'VCO', 
                             'pd':'phase_detector'})
class PNPrmtrMng():pass


class PNAskMessage():
    pass
