# -*- coding: utf-8 -*-

cipher= '“Qdt mqgq,"Wdms eq es mrkus qkoetsy sdms beqmllkejsq yku qk iuod?" Thheks sdejgq, "Kd E bkj\'s gjkw, eq es sdms wt okhhtosevthy sdkucds Qstvt Fkrq wmq m cptms imj tvtj wdtj wt gjtw dt imbt rehhekjq kaa sdt rmogq ka odehbptj? Kp imyrt es\'q sdms es atthq hegt mhh kup dtpktq mpt okujstpates; sdt wkphb esqtha\'q fuqs kjt rec dkmx. Qlmiiejc tmod ksdtp wesd kup rupjejc okiitjsmpy ka ruhhqdes imqnutpmbejc mq ejqecds, kup qkoemh itbem amgejc mq ejseimoy. Kp eq es sdms wt vkstb akp sdeq? Jks wesd kup pecctb thtosekjq, rus wesd kup sdejcq, kup lpkltpsy, kup ikjty. E\'i jks qmyejc mjysdejc jtw. Wt mhh gjkw wdy wt bk sdeq, jks rtomuqt Dujctp Cmitq rkkgq imgtq uq dmlly rus rtomuqt wt wmjjm rt qtbmstb. Rtomuqt es\'q lmejauh jks sk lptstjb, rtomuqt wt\'pt okwmpbq. Auog Qkoetsy."'
cipher = """
“Qdt mqgq,"Wdms eq es mrkus qkoetsy sdms beqmllkejsq yku qk iuod?" Thheks sdejgq, "Kd E bkj's gjkw, eq es sdms wt okhhtosevthy sdkucds Qstvt Fkrq wmq m cptms imj tvtj wdtj wt gjtw dt imbt rehhekjq kaa sdt rmogq ka odehbptj? Kp imyrt es'q sdms es atthq hegt mhh kup dtpktq mpt okujstpates; sdt wkphb esqtha'q fuqs kjt rec dkmx. Qlmiiejc tmod ksdtp wesd kup rupjejc okiitjsmpy ka ruhhqdes imqnutpmbejc mq ejqecds, kup qkoemh itbem amgejc mq ejseimoy. Kp eq es sdms wt vkstb akp sdeq? Jks wesd kup pecctb thtosekjq, rus wesd kup sdejcq, kup lpkltpsy, kup ikjty. E'i jks qmyejc mjysdejc jtw. Wt mhh gjkw wdy wt bk sdeq, jks rtomuqt Dujctp Cmitq rkkgq imgtq uq dmlly rus rtomuqt wt wmjjm rt qtbmstb. Rtomuqt es'q lmejauh jks sk lptstjb, rtomuqt wt'pt okwmpbq. Auog Qkoetsy." 



Hint: Are all letters in English used the same number of times? 


Who's she? Just knowing who's she won't get you the flag ;)
"""

unique= set(cipher)

print(unique)
print(len(unique))

key = {
    'a': 'f',
    'b': 'd',
    'c': 'g',
    'd': 'h',
    'e': 'i',
    'f': 'j',
    'g': 'k',
    'h': 'l',
    'i': 'm',
    'j': 'n',
    'k': 'o',
    'l': 'p',
    'm': 'a',
    'n': 's',
    'o': 'c',
    'p': 'r',
    'q': 's',
    'r': 'b',
    's': 't',
    't': 'e',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'y': 'y',
    'z': 'z'
}

def decode(value: str):

    if value.isalpha() and value.lower() in key :
        if value.isupper():
            return key[value.lower()].upper()
        else:
            return key[value]
    else:
        return value

plaintext = ''.join(map(decode, cipher))


print(plaintext)