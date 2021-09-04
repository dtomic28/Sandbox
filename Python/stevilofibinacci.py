def presses(phrase):
    l = [["a", "b", "c"]["d", "e", "f"]["g", "h", "i"]["j","k","l"]["m","n","o"]["p","q","r","s"]["t","u","v"]["w","x","y","z"][" "]]
    phrase = phrase.lower()
    for c in phrase:
        [(i, l.index(c)) for i, j in enumerate(l) if c in l]


presses("phrase")