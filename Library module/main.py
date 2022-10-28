from ProdSales import sales
from ProdPurchase import *

st = sales()
pt = purchase()


def proloss(st, pt):
    pl = st - pt
    if st > pt:
        print('Total profit:', pl)
    else:
        print('Total loss:', pl)


proloss(st, pt)


import ProdSales
ProdSales.sales()
