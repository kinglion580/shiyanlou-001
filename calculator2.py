#!/usr/bin/python
import sys

def con(*salar):
    wuxian = 0
    shui = 0
    try:
        salar = int(*salar)
    except Exception:
        print('Parameter Error')
        exit()
    if salar < 3500:
        print(0)
        exit()
    if salar > 3500 and salar <= 5000:
        wuxian = salar*0.165
        shui = (salar - wuxian - 3500)*0.03
    if salar > 5000 and salar <= 8000:
        wuxian = salar * 0.165
        shui = (salar - wuxian - 3500) * 0.1 - 105
    if salar > 8000 and salar <= 12500:
        wuxian = salar * 0.165
        shui = (salar - wuxian - 3500) * 0.2 - 555
    if salar > 12500 and salar <= 38500:
        wuxian = salar * 0.165
        shui = (salar - wuxian - 3500) * 0.25 - 1005
    if salar > 38500 and salar <= 58500:
        wuxian = salar * 0.165
        shui = (salar - wuxian - 3500) * 0.3 - 2755
    if salar > 58500 and salar <= 83500:
        wuxian = salar * 0.165
        shui = (salar - wuxian - 3500) * 0.35 - 5505
    if salar > 83500:
        wuxian = salar * 0.165
        shui = (salar - wuxian - 3500) * 0.45 - 13505
    return '%.2f' % (salar - wuxian - shui)

for i in range(1,len(sys.argv)):
    gonghao = sys.argv[i].split(':')[0]
    gongzi = con(sys.argv[i].split(':')[1])
    print(gonghao + ':' + gongzi)

