---
title: photoStrippedSize
description: photoStrippedSize attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoStrippedSize  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[string](../types/string.md) | Yes|
|bytes|[bytes](../types/bytes.md) | Yes|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoStrippedSize = ['_' => 'photoStrippedSize', 'type' => 'string', 'bytes' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "photoStrippedSize", "type": "string", "bytes": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
photoStrippedSize={_='photoStrippedSize', type='string', bytes='bytes'}

```


