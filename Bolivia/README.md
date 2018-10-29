# Country(200):  Bolivia
----------
Description:  Leonard keeps bragging about what a great fullstack sysadmin devop he is. Let's teach him a lesson by dumping his database password. His site is here: http://52.9.13.75:30100/
----------
Hint:  yes
----------
Attachments:  []

~!|----------|!~

Basically the website runs a really old version of wordpress, but even crustier verison
of the plugins.

We can wps scan by booting into this image right mhere

```
docker run --rm -ti  --entrypoint=/bin/sh wpscanteam/wpscan
```

Then we can run wps scan against this dude, but in particular the plugins

```
wpscan --url http://52.9.13.75:30100 --enumerate vp
```


```
[+] URL: http://52.9.13.75:30100/
[+] Started: Wed Oct 17 10:32:21 2018

Interesting Finding(s):

[+] http://52.9.13.75:30100/
 | Interesting Entries:
 |  - Server: Apache/2.4.25 (Debian)
 |  - X-Powered-By: PHP/5.6.38
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] http://52.9.13.75:30100/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[+] http://52.9.13.75:30100/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] WordPress version 4.8.2 identified.
 | Detected By: Rss Generator (Passive Detection)
 |  - http://52.9.13.75:30100/?feed=rss2, <generator>https://wordpress.org/?v=4.8.2</generator>
 |  - http://52.9.13.75:30100/?feed=comments-rss2, <generator>https://wordpress.org/?v=4.8.2</generator>
 |
 | [!] 12 vulnerabilities identified:
 |
 | [!] Title: WordPress 2.3-4.8.3 - Host Header Injection in Password Reset
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/8807
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8295
 |      - https://exploitbox.io/vuln/WordPress-Exploit-4-7-Unauth-Password-Reset-0day-CVE-2017-8295.html
 |      - http://blog.dewhurstsecurity.com/2017/05/04/exploitbox-wordpress-security-advisories.html
 |      - https://core.trac.wordpress.org/ticket/25239
 |
 | [!] Title: WordPress <= 4.8.2 - $wpdb->prepare() Weakness
 |     Fixed in: 4.8.3
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/8941
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16510
 |      - https://wordpress.org/news/2017/10/wordpress-4-8-3-security-release/
 |      - https://github.com/WordPress/WordPress/commit/a2693fd8602e3263b5925b9d799ddd577202167d
 |      - https://twitter.com/ircmaxell/status/923662170092638208
 |      - https://blog.ircmaxell.com/2017/10/disclosure-wordpress-wpdb-sql-injection-technical.html
 |
 | [!] Title: WordPress 2.8.6-4.9 - Authenticated JavaScript File Upload
 |     Fixed in: 4.8.4
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/8966
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-17092
 |      - https://wordpress.org/news/2017/11/wordpress-4-9-1-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/67d03a98c2cae5f41843c897f206adde299b0509
 |
 | [!] Title: WordPress 1.5.0-4.9 - RSS and Atom Feed Escaping
 |     Fixed in: 4.8.4
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/8967
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-17094
 |      - https://wordpress.org/news/2017/11/wordpress-4-9-1-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/f1de7e42df29395c3314bf85bff3d1f4f90541de
 |
 | [!] Title: WordPress 4.3.0-4.9 - HTML Language Attribute Escaping
 |     Fixed in: 4.8.4
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/8968
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-17093
 |      - https://wordpress.org/news/2017/11/wordpress-4-9-1-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/3713ac5ebc90fb2011e98dfd691420f43da6c09a
 |
 | [!] Title: WordPress 3.7-4.9 - 'newbloguser' Key Weak Hashing
 |     Fixed in: 4.8.4
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/8969
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-17091
 |      - https://wordpress.org/news/2017/11/wordpress-4-9-1-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/eaf1cfdc1fe0bdffabd8d879c591b864d833326c
 |
 | [!] Title: WordPress 3.7-4.9.1 - MediaElement Cross-Site Scripting (XSS)
 |     Fixed in: 4.8.5
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/9006
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5776
 |      - https://github.com/WordPress/WordPress/commit/3fe9cb61ee71fcfadb5e002399296fcc1198d850
 |      - https://wordpress.org/news/2018/01/wordpress-4-9-2-security-and-maintenance-release/
 |      - https://core.trac.wordpress.org/ticket/42720
 |
 | [!] Title: WordPress <= 4.9.4 - Application Denial of Service (DoS) (unpatched)
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/9021
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6389
 |      - https://baraktawily.blogspot.fr/2018/02/how-to-dos-29-of-world-wide-websites.html
 |      - https://github.com/quitten/doser.py
 |      - https://thehackernews.com/2018/02/wordpress-dos-exploit.html
 |
 | [!] Title: WordPress 3.7-4.9.4 - Remove localhost Default
 |     Fixed in: 4.8.6
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/9053
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-10101
 |      - https://wordpress.org/news/2018/04/wordpress-4-9-5-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/804363859602d4050d9a38a21f5a65d9aec18216
 |
 | [!] Title: WordPress 3.7-4.9.4 - Use Safe Redirect for Login
 |     Fixed in: 4.8.6
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/9054
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-10100
 |      - https://wordpress.org/news/2018/04/wordpress-4-9-5-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/14bc2c0a6fde0da04b47130707e01df850eedc7e
 |
 | [!] Title: WordPress 3.7-4.9.4 - Escape Version in Generator Tag
 |     Fixed in: 4.8.6
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/9055
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-10102
 |      - https://wordpress.org/news/2018/04/wordpress-4-9-5-security-and-maintenance-release/
 |      - https://github.com/WordPress/WordPress/commit/31a4369366d6b8ce30045d4c838de2412c77850d
 |
 | [!] Title: WordPress <= 4.9.6 - Authenticated Arbitrary File Deletion
 |     Fixed in: 4.8.7
 |     References:
 |      - https://wpvulndb.com/vulnerabilities/9100
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12895
 |      - https://blog.ripstech.com/2018/wordpress-file-delete-to-code-execution/
 |      - http://blog.vulnspy.com/2018/06/27/Wordpress-4-9-6-Arbitrary-File-Delection-Vulnerbility-Exploit/
 |      - https://github.com/WordPress/WordPress/commit/c9dce0606b0d7e6f494d4abe7b193ac046a322cd
 |      - https://wordpress.org/news/2018/07/wordpress-4-9-7-security-and-maintenance-release/
 |      - https://www.wordfence.com/blog/2018/07/details-of-an-additional-file-deletion-vulnerability-patched-in-wordpress-4-9-7/

[+] WordPress theme in use: twentyseventeen
 | Location: http://52.9.13.75:30100/wp-content/themes/twentyseventeen/
 | Last Updated: 2018-08-02T00:00:00.000Z
 | Readme: http://52.9.13.75:30100/wp-content/themes/twentyseventeen/README.txt
 | [!] The version is out of date, the latest version is 1.7
 | Style URL: http://52.9.13.75:30100/wp-content/themes/twentyseventeen/style.css?ver=4.8.2
 | Style Name: Twenty Seventeen
 | Style URI: https://wordpress.org/themes/twentyseventeen/
 | Description: Twenty Seventeen brings your site to life with header video and immersive featured images. With a fo...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Detected By: Css Style (Passive Detection)
 |
 | Version: 1.3 (80% confidence)
 | Detected By: Style (Passive Detection)
 |  - http://52.9.13.75:30100/wp-content/themes/twentyseventeen/style.css?ver=4.8.2, Match: 'Version: 1.3'

[+] Enumerating Vulnerable Plugins

[i] No plugins Found.
```

Not so helpful now is it?
Turns out that the plugins detection didnt quite work, weird, so i decided to manually check it out.

Turns out that /wp-content/plugins directory was missing index.php file, which let us browse the contents.  One of the plugins that was installed was an upload plugin, which let us upload random files into a directory that we could view from the server.  So after running that, we were able to dump the database.