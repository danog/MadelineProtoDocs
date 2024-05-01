---
title: "inputSecureFile"
description: "Pre-uploaded passport file, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFile  
[Back to constructors index](/API_docs/constructors/index.html)



Pre-uploaded [passport](https://core.telegram.org/passport) file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Secure file ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Secure file access hash|



### Type: [InputSecureFile](/API_docs/types/InputSecureFile.html)


### Example:

```
$inputSecureFile = ['_' => 'inputSecureFile', 'id' => long, 'access_hash' => long];
```  
