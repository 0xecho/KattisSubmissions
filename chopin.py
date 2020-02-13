d={
    'A':'',
    'A#':'Bb',
    'B':'',
    'C':'',
    'C#':'Db',
    'D':'',
    'D#':'Eb',
    'E':'',
    'F':'',
    'F#':'Gb',
    'G':'',
    'G#':'Ab',
    'Bb':'A#',
    'Db':'C#',
    'Eb':'D#',
    'Gb':'F#',
    'Ab':'G#',
       
}

import sys
n=1

for i in [j.split()for j in sys.stdin]:
    print(f"Case {n}:",d[i[0]]+" "+i[1] if not d[i[0]]=='' else "UNIQUE")
    n+=1