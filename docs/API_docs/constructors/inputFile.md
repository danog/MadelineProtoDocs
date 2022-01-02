---
title: "inputFile"
description: "Defines a file saved in parts using the method upload.saveFilePart."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFile  
[Back to constructors index](index.md)



Defines a file saved in parts using the method [upload.saveFilePart](../methods/upload.saveFilePart.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Random file identifier created by the client|
|parts|[int](../types/int.md) | Yes|Number of parts saved|
|name|[string](../types/string.md) | Yes|Full name of the file|
|md5\_checksum|[string](../types/string.md) | Yes|In case the file's [md5-hash](https://en.wikipedia.org/wiki/MD5#MD5_hashes) was passed, contents of the file will be checked prior to use|



### Type: [InputFile](../types/InputFile.md)


### Example:

```php
$inputFile = ['_' => 'inputFile', 'id' => long, 'parts' => int, 'name' => 'string', 'md5_checksum' => 'string'];
```  


Or, if you're into Lua:

```lua
inputFile={_='inputFile', id=long, parts=int, name='string', md5_checksum='string'}

```


