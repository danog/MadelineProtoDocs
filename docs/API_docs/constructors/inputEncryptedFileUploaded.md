---
title: "inputEncryptedFileUploaded"
description: "Sets new encrypted file saved by parts using upload.saveFilePart method."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileUploaded  
[Back to constructors index](index.md)



Sets new encrypted file saved by parts using upload.saveFilePart method.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Random file ID created by clien|
|parts|[int](../types/int.md) | Yes|Number of saved parts|
|md5\_checksum|[string](../types/string.md) | Yes|In case [md5-HASH](https://en.wikipedia.org/wiki/MD5) of the (already encrypted) file was transmitted, file content will be checked prior to use|
|key\_fingerprint|[int](../types/int.md) | Yes|32-bit fingerprint of the key used to encrypt a file|



### Type: [InputEncryptedFile](../types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFileUploaded = ['_' => 'inputEncryptedFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'key_fingerprint' => int];
```  


Or, if you're into Lua:

```lua
inputEncryptedFileUploaded={_='inputEncryptedFileUploaded', id=long, parts=int, md5_checksum='string', key_fingerprint=int}

```


