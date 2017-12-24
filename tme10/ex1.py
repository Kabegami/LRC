import definitions as d

GLOBAL_ALL_STATES = {'<','>','e','s','et','st','d','m','dt','mt','o','ot','='}

def transposeSet(S):
    b = set()
    for e in S:
        b.add(d.transpose[e])
    return b

def symetrieSet(S):
    b = set()
    for e in S:
        #print('e : ', e)
        b.add(d.symetrie[e])
    return b

def compose(e1, e2):
    #print('args e1 : {}, e2 : {}'.format(e1,e2))
    if e1 == '=':
        return set(e2)
    if e2 == '=':
        return set(e1)
    key = (e1, e2)
    if key in d.compositionBase:
        return d.compositionBase[key]
    t = (d.transpose[e2], d.transpose[e1])
    #print('t : ', t)
    if t in d.compositionBase:
        return transposeSet(d.compositionBase[t])
    k2 = (d.symetrie[e1], d.symetrie[e2])
    if k2 in d.compositionBase:
        elem = d.compositionBase[k2]
        #print('elem : ', elem)
        return symetrieSet(d.compositionBase[k2])
    k3 = (d.symetrie[d.transpose[e2]], d.symetrie[d.transpose[e1]])
    if k3 in d.compositionBase:
        v = d.compositionBase[k3]
        v3 = transposeSet(symetrieSet(v))
        return v3
    

def compositionSet(r1, r2):
    if type(r1) == 'str':
        r1 = set(r1)
    if type(r2) == 'str':
        r2 = set(r2)
    S =  set()
    for e1 in r1:
        for e2 in r2:
            S = S.union(compose(e1,e2))
    return S

def test_compositionSet():
    t1 = compositionSet('=','d')
    print('t :', t1)
    t2 = compositionSet('m','d')
    print('t2 : ', t2)
    t3 = compositionSet({'ot'},'>')
    print('t3 : ', t3)
    t4 = compositionSet('>','e')
    print('t4 : ', t4)
    t5 = compositionSet({'ot'},'m')
    print('t5 : ', t5)

if __name__ == "__main__":
    test_compositionSet()
