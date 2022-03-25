import copy
import random
import json

def getStarterArr():
    arr = []
    for a in range(9):
        i=[]
        j = tuple()
        for b in range(9):
            #j = (a,b)
            i.append('')
        arr.append(i)
        #print(i)
    return arr

def getRand():
    ra = [a for a in range(1,10)]
    random.shuffle(ra)
    return ra

def getBox(j,k,arr):
    n = set()
    for m in range(3*j,3+(3*j)):
        i=[]
        j = tuple()
        for b in range(3*k,3+(3*k)):
            l = (m,b)
            i.append(l)
            n.add(arr[m][b])
    n.discard('')
    return n

def norm(num):
    if(num<3):
        num=0
    elif(num<6):
        num=1
    else: num=2
    return num
def getHLine(aa,i):
        s = set(aa[i])
        s.discard('')
        return s
def getYLine(aa, i):
    s = set()
    for j in range(9):
        s.add(aa[j][i])
    s.discard('')
    return s
def getUpdatedLine(r, aaa,bbb):
    m = set(range(1,10))
    hLine = getHLine(aaa, r[0])
    #print('hLine', hLine)
    bbb = bbb.union(hLine)
    bbb = bbb.union(getYLine(aaa, r[1]))
    #print('b',bbb)
    n = list(m.difference(bbb))
    d = random.choice(n)
    #print(d)
    aaa[r[0]][r[1]] = d
    return aaa
def createSudoku():
    a = getStarterArr()
    a[0] = getRand()    
    for i in range(1,9):
        for j in range(9):
            c = 0
            r = (i, j)
            box = getBox(norm(i),norm(j),a)
            #print('box',box)
            res = False
            while(not res):
                c+=1
                if(c>=500):
                    break
                try:
                    getUpdatedLine(r, a, box)
                    res = True
                except (IndexError):
                    res = False
            #print('a', i,  a[i])
            if(c>=100):
                    break
        if(c>=100):
                    break

    fArr = [i,j]
    fArr.append(a)
    return fArr

def removeValues(ar, level):
    if(level == 'medium'):
        lvlrange = (3,6)
    elif(level == 'hard'):
        lvlrange = (5,8)
    elif(level == 'impossible'):
        lvlrange = (7,9)
    else:
        lvlrange = (2,4)

    for i in range(9):
        n = random.randint(lvlrange[0],lvlrange[1])
        c=0
        while(c!=n):
            ss = set(ar[i])
            ss.discard(0)
            ch = random.choice(list(ss))
            idx = ar[i].index(ch)
            ar[i].pop(idx)
            ar[i].insert(idx,0)
            c+=1
    #for i in ar:
        #print(i)
    return ar


def getSudoku(level):
    m = 0
    x = False
    while(m<1000):
        m+=1
        f = createSudoku()
        if(f[0] == 8 and f[1] == 8):
            print('Found Solution')
            x = True
            #for i in f[2]:
                #print(i)
            break
    if(not x):
        print('Try Again')
        d = dict()
        d["data"] = ""
        json_string = json.dumps(d)
    else:
        print('Sudoku Found')
        d = dict()        
        d["data"] = {'solved': f[2]}
        lis2 = copy.deepcopy(f[2])  
        d['data']['unsolved'] = removeValues(lis2, level)
        json_string = json.dumps(d)
    return json_string
    
#getSudoku('easy')