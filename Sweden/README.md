# Country(200):  Sweden
----------
Description:  Find the flag!

http://52.9.13.75:8887/upload.php
----------
Hint:  Uploading an "image" would be a "tragic" mistake!
----------
Attachments:  []

~!|----------|!~

it looks like we might need to upload an image

## The pwning

```
~ # curl -vv http://52.9.13.75:8887/upload.php                                                                                                                                                                              root@758de12c22c9
*   Trying 52.9.13.75...
* TCP_NODELAY set
* Connected to 52.9.13.75 (52.9.13.75) port 8887 (#0)
> GET /upload.php HTTP/1.1
> Host: 52.9.13.75:8887
> User-Agent: curl/7.61.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Tue, 23 Oct 2018 23:14:00 GMT
< Server: Apache/2.4.25 (Debian)
< X-Powered-By: PHP/7.1.18
< Vary: Accept-Encoding
< Content-Length: 134
< Content-Type: text/html; charset=UTF-8
<
<form method="post" enctype="multipart/form-data">
    File: <input type="file" name="file_upload">
    <input type="submit">
</form>
* Connection #0 to host 52.9.13.75 left intact
-----------------------------------------------------

```

### Invalid file upload
```
/src/ctf/Sweden(master*) # curl -vv --form file_upload=@wooh.jpg -X POST http://52.9.13.75:8887/upload.php                                                                                                                  root@758de12c22c9
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 52.9.13.75...
* TCP_NODELAY set
* Connected to 52.9.13.75 (52.9.13.75) port 8887 (#0)
> POST /upload.php HTTP/1.1
> Host: 52.9.13.75:8887
> User-Agent: curl/7.61.0
> Accept: */*
> Content-Length: 210
> Content-Type: multipart/form-data; boundary=------------------------bf615114bd8a9831
>
< HTTP/1.1 200 OK
< Date: Tue, 23 Oct 2018 23:25:21 GMT
< Server: Apache/2.4.25 (Debian)
< X-Powered-By: PHP/7.1.18
< Vary: Accept-Encoding
< Content-Length: 331
< Content-Type: text/html; charset=UTF-8
<
<br />
<b>Fatal error</b>:  Uncaught ImagickException: no decode delegate for this image format `' @ error/constitute.c/ReadImage/501 in /var/www/html/upload.php:10
Stack trace:
#0 /var/www/html/upload.php(10): Imagick-&gt;__construct('/tmp/phpakzs7u')
#1 {main}
  thrown in <b>/var/www/html/upload.php</b> on line <b>10</b><br />
* Connection #0 to host 52.9.13.75 left intact
```
### Potential exploit #1
CVE-2017-5340

Zend/zend_hash.c in PHP before 7.0.15 and 7.1.x before 7.1.1 mishandles certain cases that require large array allocations, which allows remote attackers to execute arbitrary code or cause a denial of service (integer overflow, uninitialized memory access, and use of arbitrary destructor function pointers) via crafted serialized data.

https://hackerone.com/reports/195950

## vulnerability #2
	CVE-2017-9067

# The actual exploit
Well it turns out the vulnerable part was image magic (http://imagetragick.com) which got hit but a brutal exploit.  By uploading exploit.gif, you
essentially dump the contents of the flag which ended up being.

```
CK{dee2a6f264ff91f3032a3b36b5bc3cd5237060cf}
```

