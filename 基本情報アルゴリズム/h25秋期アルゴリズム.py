def inttoalphabet(num):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return alphabet[num - 1]

def compress(plaindata,plength,compresseddata,clength):
    if plength >=1:
        esym = "$"
        pindex = 0
        cindex = 0
        while pindex < plength and pindex < 4:
            compresseddata.append(plaindata[pindex])
            cindex += 1
            pindex += 1
        while pindex < plength:
            maxfitnum = -1
            maxdistance = -1
            distance = 4
            while distance <= 26 and pindex - distance >= 0:
                fitnum = 0
                while fitnum < distance and pindex + fitnum < plength:
                    if not plaindata[pindex + fitnum] == plaindata[pindex - distance + fitnum]:
                        break
                    fitnum += 1
                if fitnum >= 4 and maxfitnum < fitnum:
                    maxfitnum = fitnum
                    maxdistance = distance
                distance += 1
            if maxfitnum == -1:
                compresseddata.append(plaindata[pindex])
                cindex += 1
                pindex += 1
            else:
                compresseddata.append(esym)
                compresseddata.append(inttoalphabet(maxdistance))
                compresseddata.append(inttoalphabet(maxfitnum))
                cindex += 3
                pindex += maxfitnum
        clength = cindex
        print(compresseddata)

plaindata = list("ABCDEFGABCDEABCDFEFGABCD")
compresseddata = []
compress(plaindata,len(plaindata),compresseddata,0)
