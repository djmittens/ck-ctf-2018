# -*- coding: utf-8 -*-
import base64
import string
import binascii
import sys


base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

text = """T2gsIEkgZG9uJ3Qga25vdy4g<br><br>
SXMgaXQgdGhhdCB3ZSBjb2xsZWN0aXZlbHkgdGhvdWdodCBTdGV2ZSBKb2JzIHdhcyBhIGdyZWF0IG1hbiwgZXZlbiB3aGVuIHdlIGtuZXcgaGUgbWFkZSBiaWxsaW9ucyBvZmYgdGhlIGJhY2tzIG9mIGNoaWxkcmVuPyD=<br><br>
T3IgbWF5YmUgaXQncyB0aGF0IGl0IGZlZWxzIGxpa2UgYWxsIG91ciBoZXJvZXMgYXJlIGNvdW50ZXJmZWl0P0==<br><br>
VGhlIHdvcmxkIGl0c2VsZuKAmXMganVzdCBvbmUgYmlnIGhvYXguIFNwYW1taW5nIGVhY2ggb3RoZXIgd2l0aCBvdXIgYnVybmluZyBjb21tZW50YXJ5IG9mIGJ1bGxzaGl0IG1hc3F1ZXJhZGluZyBhcyBpbnNpZ2h0LCBvdXIgc29jaWFsIG1lZGlhIGZha2luZyBhcyBpbnRpbWFjeS7=<br><br>
T3IgaXMgaXQgdGhhdCB3ZSB2b3RlZCBmb3IgdGhpcz8g<br><br>
Tm90IHdpdGggb3VyIHJpZ2dlZCBlbGVjdGlvbnMsIGJ1dCB3aXRoIG91ciB0aGluZ3MsIG91ciBwcm9wZXJ0eSwgb3VyIG1vbmV5Lj==<br><br>
SSdtIG5vdCBzYXlpbmcgYW55dGhpbmcgbmV3LiBXZSBhbGwga25vdyB3aHkgd2UgZG8gdGhpcywgbm90IGJlY2F1c2UgSHVuZ2VyIEdhbWVzIGJvb2tzIG1ha2VzIHVzIGhhcHB5LCBidXQgYmVjYXVzZSB3ZSB3YW5uYSBiZSBzZWRhdGVkLo==<br><br>
QmVjYXVzZSBpdCdzIHBhaW5mdWwgbm90IHRvIHByZXRlbmQsIGJlY2F1c2Ugd2UncmUgY293YXJkcyH=<br><br>
RnVjayBzb2NpZXR5Ln==<br><br>
"""

input_data = [line[:-8] for line in text.splitlines()]

def math(data, apply):
    binary = base64.b64decode(data)
    reenc = base64.b64encode(binary)
    return apply(data, reenc)

# take_two_bits = lambda x: x & 3
# take_four_bits = lambda x: x & 15
diff_two = lambda d: math(d, lambda a, b: abs(ord(a[-2]) - b[-2]))
diff_four = lambda d: math(d, lambda a, b: abs(ord(a[-3]) - b[-3]) & 15)
hidden_padding = lambda s: diff_four(s) if s[-2:] == "==" else diff_two(s)

def analyze(b64):
    select_second = lambda x, y: y
    print('Original: %s' % b64)
    print('Recoded : %s' % str(math(b64, select_second), 'utf-8'))
    print('Decoded : %s' % str(base64.b64decode(b64), 'utf-8'))
    print('Hidden Bits(4): %s' % hidden_padding(b64))

for i in input_data:
    analyze(i)
    print('--------------------------------------')

res = []
for i in input_data:
    padding = hidden_padding(i)
    if(padding == 0):
        res.append('-')
    else:
        res.append(base64chars[abs(padding)])

print(''.join(res))

def get_padding(x):
    if(x[-2:] == '=='):
        return base64chars.index(x[-3]) & 31
    elif(x[-1] == '='):
        return base64chars.index(x[-2]) & 3
    else:
        return 0


res = []
for i in input_data:
    padding = get_padding(i)
    print(len(i) % 4)
    if(padding == 0):
        res.append('-')
    else:
        res.append('{0:b}'.format(padding))
print(res)
# print(''.join(res))
# print([base64chars[hidden_padding(i)] for i in input_data])

# decode 4-byte integral
def decode_integral(integral, padding):
    if(len(integral) != 4):
        raise TypeError("Integral was not the right size: %s" % integral)
        
    # figure out the right bits
    def getint(x) : 
        try: 
            return base64chars.index(x)
        except:
            print ("Couldnt lookup character in base64 table: %s" % x)
            return 0
    one = getint(integral[0])
    two = getint(integral[1])
    three = getint(integral[2])
    four = getint(integral[3])
    
    pad_mask = sys.maxsize - 1
    if padding == 4:
        hidden = ord(integral[1]) & 15
        print('{0:b}'.format(hidden))
        pad_mask = pad_mask << 4

    elif padding == 2:
        hidden = ord(integral[2]) & 3
        print('{0:b}'.format(hidden))
        pad_mask = pad_mask << 2

    # will make 3 bytes out of 4
    result = []
    
    result.append(chr(((one << 2) | (two >> 4)) & 255))
    result.append(chr(((two << 4) | (three >> 2)) & 255))
    result.append(chr(((three << 6) | (four)) & 255))

    return result


def decode_base64(st):
    if(len(st) % 4 != 0):
        raise TypeError('It seems like the string doesnt have 4 whole base64 integrals and thefore invalid')
    
    if(st[-2:] == '=='):
        padding = 4
    elif(st[-1] == '='):
        padding = 2 
    else:
        padding = 0

    res = []
    # break into chunks
    for i in range(0, len(st), 4):  
        chunk = st[i:i + 4]
        # if last integral signal padding.
        pad = padding if i + 4 == len(st) else 0
        res.extend(decode_integral(chunk, pad))  

    return ''.join(res)

# print(decode_base64(input_data[3]))
for i in input_data:
    print(decode_base64(i))



for encoded in input_data:
    recoded = str(base64.b64encode(base64.b64decode(encoded)), 'utf-8')

    diffs = [ord(b) - ord(a) for a, b in zip(encoded, recoded)]

    def rel (x):
        if x == 0:
            return 0
        else:
            return 1
    # print(encoded)
    # print(recoded)
    result = zip(diffs, encoded)
    result = map(lambda x: x[1] if x[0] else 0, result)
    result = filter(lambda x: x != 0, result)
    print(list(result))


# -D07-joH-
print(str(base64.b64encode(base64.b64decode(input_data[8])), 'utf-8'))