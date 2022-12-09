def index(alphabet):
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return alpha.index(alphabet)

def generatebitmask(pat,mask):
    patlen = len(pat)
    for i in range(0,26,1):
        mask.append(0b0)
    for i in range(0,patlen,1):
        mask[index(pat[i])] = (0b1 << i) | mask[index(pat[i])]
    return patlen

def ganeratebitmaskregex(pat,mask):
    originalpatlen = len(pat)
    patlen = 0
    mode = 0
    for i in range(0,26,1):
        mask.append(0b0)
    for i in range(0,originalpatlen,1):
        if pat[i] == "[":
            mode = 1
            patlen += 1
        else:
            if pat[i] == "]":
                mode = 0
            else:
                if mode == 0:
                    patlen += 1
                mask[index(pat[i])] = 0b1 << (patlen - 1) | mask[index(pat[i])]
    print("patlen=",patlen)
    return patlen
                
def bitapmatch(text,pat):
    mask = []
    textlen = len(text)
    patlen = generatebitmask(pat,mask)
    print(mask)
    status = 0b0
    goal = 0b1 << (patlen - 1)
    for i in range(0,textlen,1):
        print("i=",i)
        status = (status << 1) | 0b1
        print("status=",status)
        print("mask[index(text[i])]=",mask[index(text[i])])
        status = status & mask[index(text[i])]
        print("status2=",status)
        if not status & goal  == 0b0:
            return (i - patlen + 1)
    return -1

def bitapmatch2(text,pat):
    mask = []
    textlen = len(text)
    patlen = ganeratebitmaskregex(pat,mask)
    print(mask)
    status = 0b0
    goal = 0b1 << (patlen - 1)
    for i in range(0,textlen,1):
        print("i=",i)
        status = (status << 1) | 0b1
        print("status=",status)
        print("mask[index(text[i])]=",mask[index(text[i])])
        status = status & mask[index(text[i])]
        print("status2=",status)
        if not status & goal  == 0b0:
            return (i - patlen + 1)
    return -1

text = list("AACBBAACABABAB")
pat = list("ACABAB")

#print(bitapmatch(text,pat))

pat = list("AC[BA]A[ABC]A")

#print(bitapmatch2(text,pat))

pat = list("AC[B[AB]AC]A")

print(bitapmatch2(text,pat))
