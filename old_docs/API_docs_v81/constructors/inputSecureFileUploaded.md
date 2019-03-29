---
title: inputSecureFileUploaded
description: Secure file uploaded
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileUploaded  
[Back to constructors index](index.md)



Secure file uploaded

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|parts|[int](../types/int.md) | Yes|Parts|
|md5\_checksum|[string](../types/string.md) | Yes|Md5 checksum|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [InputSecureFile](../types/InputSecureFile.md)


### Example:

```php
$inputSecureFileUploaded = ['_' => 'inputSecureFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
inputSecureFileUploaded={_='inputSecureFileUploaded', id=long, parts=int, md5_checksum='string', file_hash='bytes', secret='bytes'}

```


