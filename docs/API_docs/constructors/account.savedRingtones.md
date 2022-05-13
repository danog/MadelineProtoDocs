---
title: "account.savedRingtones"
description: "account.savedRingtones attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_savedRingtones.html
---
# Constructor: account.savedRingtones  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|ringtones|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [account.SavedRingtones](/API_docs/types/account.SavedRingtones.html)


### Example:

```
$account_savedRingtones = ['_' => 'account.savedRingtones', 'hash' => long, 'ringtones' => [Document, Document]];
```  
