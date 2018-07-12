---
title: inputSecureFileUploaded
description: inputSecureFileUploaded attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileUploaded  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|parts|[int](../types/int.md) | Yes|
|md5\_checksum|[string](../types/string.md) | Yes|
|file\_hash|[bytes](../types/bytes.md) | Yes|
|secret|[bytes](../types/bytes.md) | Yes|



### Type: [InputSecureFile](../types/InputSecureFile.md)


### Example:

```
$inputSecureFileUploaded = ['_' => 'inputSecureFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputSecureFileUploaded", "id": long, "parts": int, "md5_checksum": "string", "file_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secret": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
inputSecureFileUploaded={_='inputSecureFileUploaded', id=long, parts=int, md5_checksum='string', file_hash='bytes', secret='bytes'}

```


