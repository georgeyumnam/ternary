
# coding: utf-8

# In[9]:

import csv
import itertools
from zipfile import ZipFile

from pymatgen import Element, MPRester
def ternary_system():
        first_el = {el.symbol for el in Element
                    if el in ("Be", "Mg", "Sr", "Ca")}
        second_el = {el.symbol for el in Element
                    if el in ("Si", "Ge", "Sn")}
        third_el = {el.symbol for el in Element
                    if el in ("P", "As")}
        return sorted(["{}-{}".format(*sorted(triad))
                    for triad in itertools.product(first_el, second_el, third_el)])
    
mpr = MPRester("MAPI_KEY")
docs = mpr.query({'chemsys': {'$in': ternary_system()}}, ['material_id', 'pretty_formula','cif'])

with ZipFile('ternay_cifs.zip', 'w') as f:
    for d in docs:
        f.writestr('{}_{}_{}.cif'.format(d['pretty_formula'], d['material_id']),
                   d['cif'])

