---
title: encryptedFile
description: Encrypted file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedFile  
[Back to constructors index](index.md)



Encrypted file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|size|[int](../types/int.md) | Yes|Size|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|key\_fingerprint|[int](../types/int.md) | Yes|Key fingerprint|



### Type: [EncryptedFile](../types/EncryptedFile.md)


### Example:

```php
$encryptedFile = ['_' => 'encryptedFile', 'id' => long, 'access_hash' => long, 'size' => int, 'dc_id' => int, 'key_fingerprint' => int];
```  


Or, if you're into Lua:

```lua
encryptedFile={_='encryptedFile', id=long, access_hash=long, size=int, dc_id=int, key_fingerprint=int}

```


