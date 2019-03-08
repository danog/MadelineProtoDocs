---
title: inputEncryptedFileLocation
description: Encrypted file location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileLocation  
[Back to constructors index](index.md)



Encrypted file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputEncryptedFileLocation = ['_' => 'inputEncryptedFileLocation', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputEncryptedFileLocation", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputEncryptedFileLocation={_='inputEncryptedFileLocation', id=long, access_hash=long}

```


