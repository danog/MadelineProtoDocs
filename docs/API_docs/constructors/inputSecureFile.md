---
title: inputSecureFile
description: inputSecureFile attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFile  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputSecureFile](../types/InputSecureFile.md)


### Example:

```
$inputSecureFile = ['_' => 'inputSecureFile', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputSecureFile", "id": long, "access_hash": long}
```


Or, if you're into Lua:  


```
inputSecureFile={_='inputSecureFile', id=long, access_hash=long}

```


