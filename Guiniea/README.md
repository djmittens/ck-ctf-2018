# Country(100):  Guinea
----------
Description:  U3ludCUzQSUyMFBYJTdCMDc0cjkxcjYxbzIxcTQ0cjc1cG4zcHNzNXA3MzVxcjI2cDNwMHIzcSU3RAo=
----------
Hint:  no
----------
Attachments:  []
~!|----------|!~

The string looks like its url and then base 64 encoded, so we undo that with the following command

```
echo U3ludCUzQSUyMFBYJTdCMDc0cjkxcjYxbzIxcTQ0cjc1cG4zcHNzNXA3MzVxcjI2cDNwMHIzcSU3RAo= | base64 -D |  python -c "import sys, urllib as ul; print ul.unquote(sys.stdin.read());" > flag.txt
```
At first the output looks like garbage but then it gets interesting, because if you notice PX{} looks very similar to other flags which is 
CK{}  and turns out its just a linear shift up by 12.  So i created a small python script to do that which yielded the following.

```
➜  Guiniea git:(master) ✗ ./searcher.py
Flag-CK{#*'e,$e)$b%$d''e*(ca&cff(c*&(de%)c&c#e&d}
```
thats not quite it but very close.

Another interesting tool that came to my attention has been [CyberChef](https://gchq.github.io/CyberChef/)

either case this thing is called ROT-13 algorithm 
applying it will actually give you the real flag