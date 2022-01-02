---
title: "inputSecureFile"
description: "Preuploaded passport file, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFile  
[Back to constructors index](index.md)



Preuploaded [passport](https://core.telegram.org/passport) file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Secure file ID|
|access\_hash|[long](../types/long.md) | Yes|Secure file access hash|



### Type: [InputSecureFile](../types/InputSecureFile.md)


### Example:

```php
$inputSecureFile = ['_' => 'inputSecureFile', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputSecureFile={_='inputSecureFile', id=long, access_hash=long}

```


