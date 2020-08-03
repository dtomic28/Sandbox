def najdaljsaInNajkrajsaBeseda(seznam):
    dic = {}
    for i in seznam:
        if i not in dic:
            dic[i] = len(i)
    najD = {'b': "", 'd': 0}
    najK = {'b': "", "d": 9999999}
    for k,v in dic.items():
        if v > najD['d']:
            najD['b'] = k
            najD['d'] = v
        elif v < najK['d']:
            najK['b'] = k
            najK['d'] = v
    print('Najdaljsa beseda je %s, najkrajsa pa %s' %(najD['b'], najK['b']))

vnos = input('Vnesite').split()
najdaljsaInNajkrajsaBeseda(vnos)