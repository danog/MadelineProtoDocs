---
title: inputFileBig
description: Assigns a big file (over 10Mb in size), saved in part using the method [upload.saveBigFilePart](../methods/upload.saveBigFilePart.md).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileBig  
[Back to constructors index](index.md)



Assigns a big file (over 10Mb in size), saved in part using the method [upload.saveBigFilePart](../methods/upload.saveBigFilePart.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Random file id, created by the client|
|parts|[int](../types/int.md) | Yes|Number of parts saved|
|name|[string](../types/string.md) | Yes|Full file name|



### Type: [InputFile](../types/InputFile.md)


### Example:

```php
$inputFileBig = ['_' => 'inputFileBig', 'id' => long, 'parts' => int, 'name' => 'string'];
```  


Or, if you're into Lua:

```lua
inputFileBig={_='inputFileBig', id=long, parts=int, name='string'}

```


