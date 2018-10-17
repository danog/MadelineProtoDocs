---
title: inputEncryptedFile
description: inputEncryptedFile attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFile  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputEncryptedFile](../types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFile = ['_' => 'inputEncryptedFile', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputEncryptedFile", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputEncryptedFile={_='inputEncryptedFile', id=long, access_hash=long}

```


