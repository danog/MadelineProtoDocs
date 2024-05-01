---
title: "account.savedRingtoneConverted"
description: "The notification sound was not in MP3 format and was successfully converted and saved, use the returned Document to refer to the notification sound from now on"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_savedRingtoneConverted.html
---
# Constructor: account.savedRingtoneConverted  
[Back to constructors index](/API_docs/constructors/index.html)



The notification sound was not in MP3 format and was successfully converted and saved, use the returned [Document](../types/Document.html) to refer to the notification sound from now on

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[Document](/API_docs/types/Document.html) | Optional|The converted notification sound|



### Type: [account.SavedRingtone](/API_docs/types/account.SavedRingtone.html)


### Example:

```
$account_savedRingtoneConverted = ['_' => 'account.savedRingtoneConverted', 'document' => Document];
```  
