# Country(200):  Svalbard & Jan Mayen
----------
Description:  You can find the challenge here: https://code.corp.creditkarma.com/ck-private/sec_capture-the-flag/blob/master/CryptoKnight/problem_statement.markdown 

The flag to this challenge is the unicode string in the decrypted blob (as unicode). 

i.e. The flag is in this format: "\uxxxx\uxxxx\uxxxx". 

So if the decrypted blob is "\uthis\unott\upass", then \uthis\unott\upass is the flag.
----------
Hint:  Follow the spec. If you did, make sure the flag is in the right format
----------
Attachments:  []

~!|----------|!~

Man this one is the most intense challenge so far.

## Clifford notes
* It seems like there a `salted master password` (user password)  thats `md5 hashed` and `is used for AES encryption` of the user data in the database.
* The salt is 4 characters with a $ at the end.


After a lot of messing around i have implemented the complete spec, and dumped all of the files in the database, after closer review, i was lead astray by the message, and the contents were not indeed in valid json format, but that doesnt matter because there indeed some unicode excapes, in unicode file, and here they are

```
"cool: \u2603\u2744\u2746"
```

and thats it thats the answer, i wish instead of cool: they had flag: because i skipped right over this part, and wasted a bunch of time.