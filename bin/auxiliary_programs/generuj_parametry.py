#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = ["param_%i" % (i) for i in range(1, 46) ]

print (", ".join(lista))

for i in range(1, 46):
    print( "param_%i = trial.suggest_float('param_%i', -5, 5)" % (i, i)  )