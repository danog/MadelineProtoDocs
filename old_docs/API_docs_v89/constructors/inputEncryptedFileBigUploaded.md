---
title: inputEncryptedFileBigUploaded
description: Encrypted file big uploaded
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileBigUploaded  
[Back to constructors index](index.md)



Encrypted file big uploaded

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|parts|[int](../types/int.md) | Yes|Parts|
|key\_fingerprint|[int](../types/int.md) | Yes|Key fingerprint|



### Type: [InputEncryptedFile](../types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFileBigUploaded = ['_' => 'inputEncryptedFileBigUploaded', 'id' => long, 'parts' => int, 'key_fingerprint' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputEncryptedFileBigUploaded", "id": long, "parts": int, "key_fingerprint": int}
```


Or, if you're into Lua:

```lua
inputEncryptedFileBigUploaded={_='inputEncryptedFileBigUploaded', id=long, parts=int, key_fingerprint=int}

```


