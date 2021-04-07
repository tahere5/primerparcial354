# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:06:23 2021

@author: Hp
"""

from kanren import run,var
x = var()
y = var()
z = var()

from kanren import Relation,facts,conde
parent = Relation()

facts(parent,
('isidro','daniel'),
('isidro','hilda'),
('ana','daniel'),
('ana','hilda'),
('elena','betza'),
('elena','severo'),
('elena','julia'),
('daniel','tahere'),
('daniel','didar'),
('betza','tahere'),
('betza','didar'),
('severo','elisa'),
('jazmin','elisa'),
('julia','marifer'),
('julia','jose'),
('hilda','maria'),
('julio','maria'),
('maria','guadalupe'),
('nelson','guadalupe')
)

def abuelos(x, z):
    y = var()
    return conde((parent(x,y), parent(y,z) ))

def tios(x, z):
    y = var()
    w = var()
    vtios=set(run(10, x, conde((parent(y,x), parent(y,w), parent(w,z)))))
    p=list(run(10, x, parent(x, z)))
    for i in p:
        vtios.discard(i)
    return vtios
    
def hermanos(x,w):
    vhermanos=set(run(10, x, conde((parent(y,x), parent(y,w) ))))
    vhermanos.discard(w)
    return vhermanos

def hijos(x,w):
    return (parent(x,w))

def primos(x,w):
    y = var()
    j = var()
    k = var()
    l = var()
    
    vprimos=set(run(10, x, conde((parent(y,x), parent(j,w), parent(k,y),parent(k,j)))))
    hermano=hermanos(l,w)
    for i in hermano:
        vprimos.discard(i)
    vprimos.discard(w)
    return vprimos

print(run(10, x, abuelos(x, 'tahere')))
print(tios(x, 'tahere'))
print(hermanos(x, 'daniel'))
print(run(10, x, hijos('betza',x)))
print(primos(x,'tahere'))