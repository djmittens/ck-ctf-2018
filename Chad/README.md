# Country(300):  Chad
----------
Description:  You acquired a file of ~100k W-4 forms on the dark web for ₿0.01. Find Ken's SSN, based on publicly-available information.

(Actually, it's not Ken's SSN. It's just the only one in the file that could be his.)
----------
Hint:  What can LWinkipMedianum tell you about Ken in 2005? in 1979?
----------
Attachments:  [{'filename': '2005_W4_3ab3c199574f85961ffe70e2f5a5da16.CSV.gz', 'file_link': '/data/attachment.php?id=4'}]
~!|----------|!~

We got a bunch of stuff from darkweb, and we need to find kens SSN based on publicly available information.

ok so looks like a lot of the fields are hashed, ironically tho, SSN's arent

we have a 5 digit field thats not hashed that is probably a zip code, so lets filter it!
since we know Ken lived in california in 2015 we can filter on those  down by a lot

```
 cat 2005_W4_3ab3c199574f85961ffe70e2f5a5da16.CSV| egrep "^.*'9[0-5][0-9]{3}'.*$"
```

not bad that narrowed it down to  6461 matches.

now lets see if we can get some hash collisions(hopefully unsalted) on kens last name `Lin` or `lin`

```
➜  Chad git:(master) ✗ md5 -s Lin
MD5 ("Lin") = b3cd9344dad3ff77b4fd532b70660aa2
➜  Chad git:(master) ✗ md5 -s lin
MD5 ("lin") = c93169f1eb9be7246f990690b5e66b2d
➜  Chad git:(master) ✗
```

hmm interesting so it seems like either the fields dont contain names, or perhaps the hashes are salted.
moving on.

e-loan ein
```
77-0460084
```

which was purchased (and closed in fourth quarter) by Popular inc
```
66-0667416
```

needless to say neither ein was found in this dumpster.

so ther eare multiple eins for that company and the right one was this

```
cat possibles.csv|grep "'530-" |  grep 66-0416582
```

which gave us fake kens ssn as follows

```
530-90-5699
```