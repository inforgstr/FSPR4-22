def encode(d):
    en = []
    ed = []
    counter = 0
    for i in range(len(d)+1):
        if counter == len(d)+2:
            break
        if counter < int((len(d))/2):
            en.append(d[counter])
        if len(d) > counter >= int((len(d))/2):
            ed.append(d[counter])
        
        counter += 1
    ed.reverse()
    p = []
    b = 0
    for i in range(len(en)+1):
        # if b > len(en)-1:
        #     break
        if b < len(en) and b < len(ed):
            p.append(f'{en[b]}{ed[b]}')

        elif b == len(ed)-1:
            p.append(f'{ed[b]}')
    
        b += 1
    return ''.join(p)



def decode(n):
    en = []
    ed = []
    counter = 0
    for i in range(len(n)+1):
        if counter == len(n)+2:
            break
        if counter < int((len(n))/2):
            en.append(n[counter])
        if len(n) > counter >= int((len(n))/2):
            ed.append(n[counter])
        
        counter += 1
    print(en, ed)
    p = []
    b = 0
    for i in range(len(en)+1):
        if b > len(en):
            break
        if b == 0 or b%2==0 and b < len(en):
            p.append(f'{en[b]}')
            p.append(f'{ed[b]}')
        b += 1 
    print()
    ed.reverse()
    en.reverse()
    v = 0
    for i in range(len(ed)+1):
        if v > len(en):
            break
        if v == 0 or v %2 == 0 and v < len(en):
            p.append(f'{ed[v]}')
            p.append(f'{en[v]}')
        v += 1
    print(p)
    v = 0
    b = []
    en = []
    for i in range(len(p)+1):
        if v == len(p)+2:
            break
        if v < int((len(p))/2):
            b.append(p[v])
        if len(p) > v >= int((len(p))/2):
            en.append(p[v])
        v += 1
    print(b, en)
    counter = 0
    bn = []
    for i in range(len(b)+1):
        if counter > len(b)+2:
            break
        if counter < len(b):
            if counter == len(b)-2:
                break
            if counter == 0:
                bn.append(b[counter])
            if counter % 2 == 0:
                bn.append(b[counter+2])
            if counter == 1:
                bn.append(b[counter])
            if counter % 2 != 0:
                bn.append(b[counter+2])
        counter += 1
    print(bn)
    r = 0
    be = []
    for i in range(len(en)+1):
        if r > len(en)+2:
            break
        if r < len(en):
            if r == len(en)-2:
                break
            if r == 0:
                be.append(en[r])
            if r % 2 == 0:
                be.append(en[r+2])
            if r == 1:
                be.append(en[r])
            if r % 2 != 0:
                be.append(en[r+2])
        r += 1
    h = ''.join(bn)
    g = ''.join(be)
    print(h+g)

    

print(encode('codewars'))
decode('wehti')