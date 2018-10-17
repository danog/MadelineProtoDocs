---
title: inputFileBig
description: inputFileBig attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileBig  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|parts|[int](../types/int.md) | Yes|
|name|[string](../types/string.md) | Yes|



### Type: [InputFile](../types/InputFile.md)


### Example:

```php
$inputFileBig = ['_' => 'inputFileBig', 'id' => long, 'parts' => int, 'name' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputFileBig", "id": long, "parts": int, "name": "string"}
```


Or, if you're into Lua:

```lua
inputFileBig={_='inputFileBig', id=long, parts=int, name='string'}

```


