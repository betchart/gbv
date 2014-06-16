import zipfile


def sumweights(fp):
    sw = 0
    n = 0
    fields = str(fp.readline()).split(',')
    indices = dict((key, fields.index(key)) for key in ['SEX','ST','PWGTP'])
    for line in fp:
        entries = str(line).split(',')
        if int(entries[indices['ST']])==36:
            if int(entries[indices['SEX']])==1:
                sw += int(entries[indices['PWGTP']])
                n += 1
    return sw, n


zfname = 'csv_pus.zip'
ifnames = ['ss12pus%s.csv'%s for s in 'abcd'[2:3]] # Hack 1: NY==36 is only in file 'c', so don't loop over the other files                                                                       

zf = zipfile.ZipFile(zfname)
sws = [sumweights(zf.open(ifname)) for ifname in ifnames]
print([sum(L) for L in zip(*sws)])


