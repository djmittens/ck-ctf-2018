# Country(60):  Argentina
----------
Description:  John left this archive in a shared folder, visible by you. See if you can extract the key.

The answer will look like "CTF{contents}".
----------
Hint:  yes
----------
Attachments:  [{'filename': 'passwords_66a8db334b301b8bb6d73899f3fd3a4a.bz2', 'file_link': '/data/attachment.php?id=1'}]

~!|----------|!~
## The file
It appears to be encoded multiple times, as in, an archive inside an archive.
You can tell them apart by analyzing the hex dump.

you can see the full table [here](https://en.wikipedia.org/wiki/List_of_file_signatures)

|Magic|Type|
|-|-|
|`42 5A 68` | Bzip2|
|`1F 8B` | Gzip|
|`50 4B 03 04`| Zip |

And ofcourse after realizing that, you can proceed to extract the files in that order.

(if it helps there is a hexdump extension for VSCode which will let you figure this out right quick.)

## Decrypting zip
After receiving the final zip file you will now have the next stage of the challenge.
Which is that this stupid thing is encrypted with a password.  To extract it we will use `rockyou.txt` dictionary, and brute force it on kali.

Load up john the ripper, by first hashing the zip file

```
zip2john ps.zip > ps.hash
```

And then let john rip with its default algorithm,
```
john ps.hash
```

Ofcourse that will take forever (but hopefully the trashcan at work will help)

it is taking 10 + hours now, time to up the ante, as this password list was not enough

```
 fcrackzip -u -v -D -p /usr/share/wordlists/rockyou.txt ps.zip
```

way too slow

turns out the actual hint was that 