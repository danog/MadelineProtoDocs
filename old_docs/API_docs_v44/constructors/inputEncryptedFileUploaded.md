---
title: inputEncryptedFileUploaded
description: Encrypted file uploaded
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileUploaded  
[Back to constructors index](index.md)



Encrypted file uploaded

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|parts|[int](../types/int.md) | Yes|Parts|
|md5\_checksum|[string](../types/string.md) | Yes|Md5 checksum|
|key\_fingerprint|[int](../types/int.md) | Yes|Key fingerprint|



### Type: [InputEncryptedFile](../types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFileUploaded = ['_' => 'inputEncryptedFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'key_fingerprint' => int];
```  


Or, if you're into Lua:

```lua
inputEncryptedFileUploaded={_='inputEncryptedFileUploaded', id=long, parts=int, md5_checksum='string', key_fingerprint=int}

```


