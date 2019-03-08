---
title: inputFile
description: File
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFile  
[Back to constructors index](index.md)



File

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|parts|[int](../types/int.md) | Yes|Parts|
|name|[string](../types/string.md) | Yes|Name|
|md5\_checksum|[string](../types/string.md) | Yes|Md5 checksum|



### Type: [InputFile](../types/InputFile.md)


### Example:

```php
$inputFile = ['_' => 'inputFile', 'id' => long, 'parts' => int, 'name' => 'string', 'md5_checksum' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputFile", "id": long, "parts": int, "name": "string", "md5_checksum": "string"}
```


Or, if you're into Lua:

```lua
inputFile={_='inputFile', id=long, parts=int, name='string', md5_checksum='string'}

```


