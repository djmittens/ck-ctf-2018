# Country(700):  India
----------
Description:  http://172.30.13.219/
----------
Hint:  https://tools.ietf.org/html/rfc4648#page-5
----------
Attachments:  []
~!|----------|!~

![screenshot](screenshot.png)

Ok so initial look at our message we dont seee a whole lot.

It looks like a cypher either ROT-13 or ceasar.

The hint is not really helpful either. This one is going to be a doozy

## Look at this stuff tho.

upon further analysis the cipher appears to be encoded using simple substitution, so lets do some letter frequency analysis.

Ok so i discovered the key, but i am still not closer to figuring out the flag :O

```
“She asks,"What is it about society that disappoints you so much?" Elliot thinks, "Oh I don't know, is it that we collectively thought Steve Jobs was a great man even when we knew he made billions off the backs of children? Or maybe it's that it feels like all our heroes are counterfeit; the world itself's just one big hoax. Spamming each other with our burning commentary of bullshit massuerading as insight, our social media faking as intimacy. Or is it that we voted for this? Not with our rigged elections, but with our things, our property, our money. I'm not saying anything new. We all know why we do this, not because Hunger Games books makes us happy but because we wanna be sedated. Because it's painful not to pretend, because we're cowards. Fuck Society."



Lmse: Fbi fpp pieeibt ms Iskpmtl utih eli tfai suadib cj emait?


Wlc't tli? Nute oscwmsk wlc't tli wcs'e kie ycu eli jpfk ;)
```


Holy guacamole, this is from mr.robot,
in fact after googling it i found that it refers to krysta.  Knowing that she is definitely not the flag, i ventured on, and what luck !!! seems like her name was literally the next step (or the url)

```
➜  India git:(master) ✗ curl -vv http://172.30.13.219/krista
*   Trying 172.30.13.219...
* TCP_NODELAY set
* Connected to 172.30.13.219 (172.30.13.219) port 80 (#0)
> GET /krista HTTP/1.1
> Host: 172.30.13.219
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Wed, 24 Oct 2018 10:39:09 GMT
< Server: Apache/2.4.6 (CentOS)
< Last-Modified: Tue, 23 Oct 2018 19:06:00 GMT
< ETag: "161-578ea0f7217e5"
< Accept-Ranges: bytes
< Content-Length: 353
< Content-Type: text/plain; charset=UTF-8
<
 “What I'm about to tell you is top secret. A conspiracy bigger than all of us. There's a powerful group of people out there that are secretly running the world. I'm talking about the guys no one knows about, the ones that are invisible. The top 1% of the top 1%, the guys that play God without permission. And now I think they're following me.”

```


this quote was said by elliot so i tried again

```
➜  India git:(master) ✗ curl -vv http://172.30.13.219/elliot
*   Trying 172.30.13.219...
* TCP_NODELAY set
* Connected to 172.30.13.219 (172.30.13.219) port 80 (#0)
> GET /elliot HTTP/1.1
> Host: 172.30.13.219
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Wed, 24 Oct 2018 10:57:41 GMT
< Server: Apache/2.4.6 (CentOS)
< Last-Modified: Wed, 24 Oct 2018 02:11:35 GMT
< ETag: "4f0-578f0017baab8"
< Accept-Ranges: bytes
< Content-Length: 1264
<
T2gsIEkgZG9uJ3Qga25vdy4g<br><br>
SXMgaXQgdGhhdCB3ZSBjb2xsZWN0aXZlbHkgdGhvdWdodCBTdGV2ZSBKb2JzIHdhcyBhIGdyZWF0IG1hbiwgZXZlbiB3aGVuIHdlIGtuZXcgaGUgbWFkZSBiaWxsaW9ucyBvZmYgdGhlIGJhY2tzIG9mIGNoaWxkcmVuPyD=<br><br>
T3IgbWF5YmUgaXQncyB0aGF0IGl0IGZlZWxzIGxpa2UgYWxsIG91ciBoZXJvZXMgYXJlIGNvdW50ZXJmZWl0P0==<br><br>
VGhlIHdvcmxkIGl0c2VsZuKAmXMganVzdCBvbmUgYmlnIGhvYXguIFNwYW1taW5nIGVhY2ggb3RoZXIgd2l0aCBvdXIgYnVybmluZyBjb21tZW50YXJ5IG9mIGJ1bGxzaGl0IG1hc3F1ZXJhZGluZyBhcyBpbnNpZ2h0LCBvdXIgc29jaWFsIG1lZGlhIGZha2luZyBhcyBpbnRpbWFjeS7=<br><br>
T3IgaXMgaXQgdGhhdCB3ZSB2b3RlZCBmb3IgdGhpcz8g<br><br>
Tm90IHdpdGggb3VyIHJpZ2dlZCBlbGVjdGlvbnMsIGJ1dCB3aXRoIG91ciB0aGluZ3MsIG91ciBwcm9wZXJ0eSwgb3VyIG1vbmV5Lj==<br><br>
SSdtIG5vdCBzYXlpbmcgYW55dGhpbmcgbmV3LiBXZSBhbGwga25vdyB3aHkgd2UgZG8gdGhpcywgbm90IGJlY2F1c2UgSHVuZ2VyIEdhbWVzIGJvb2tzIG1ha2VzIHVzIGhhcHB5LCBidXQgYmVjYXVzZSB3ZSB3YW5uYSBiZSBzZWRhdGVkLo==<br><br>
QmVjYXVzZSBpdCdzIHBhaW5mdWwgbm90IHRvIHByZXRlbmQsIGJlY2F1c2Ugd2UncmUgY293YXJkcyH=<br><br>
RnVjayBzb2NpZXR5Ln==<br>
<br><br><br><br>
Hint: reality is an illusion the universe is a hologram ;) Don't believe what you see. Something's not right. <br><br>

Once you've found what's not right you'll need to create the flag from what's changed. If nothing's changed give it a "-"
* Connection #0 to host 172.30.13.219 left intact
```

fast forward many sweaty hours of base64ing (guh),
turns out the trick was very simple.  Some information is hidden inside of the paddin in this message.  How can you tell?  well you just need to decode / re-encode each line and take the difference (subtract) according to the spec it should be nothing, because the last bits (the ones that arent available to complete the 4 byte integral) should be 0 (but arent).

and so we get these
```
['-', '11', '10100', '11', '-', '11', '1000', '11', '111']
```

as the bits, and if there was no difference we get the `-`

now what do we do with this information?

nothing!
turns out the answer is that we need to take the original character that was there in the lines that changed :facepalm: and throw away all this cool hidden shit

```
[]
['D']
['0']
['7']
[]
['j']
['o']
['H']
['n']
```

all of this was done in elliot.py

which is basically the flag

```
-D07-joHn
```

whaaaay was this hard?