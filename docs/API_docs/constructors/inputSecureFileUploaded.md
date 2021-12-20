---
title: "inputSecureFileUploaded"
description: "Uploaded secure file, for more info see the passport docs »"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileUploaded  
[Back to constructors index](index.md)



Uploaded secure file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Secure file ID|
|parts|[int](../types/int.md) | Yes|Secure file part count|
|md5\_checksum|[string](../types/string.md) | Yes|MD5 hash of encrypted uploaded file, to be checked server-side|
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


