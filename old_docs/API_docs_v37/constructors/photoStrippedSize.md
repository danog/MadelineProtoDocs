---
title: photoStrippedSize
description: Just the image's content
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoStrippedSize  
[Back to constructors index](index.md)



Just the image's content

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Thumbnail type|
|bytes|[bytes](../types/bytes.md) | Yes|Thumbnail data|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoStrippedSize = ['_' => 'photoStrippedSize', 'type' => 'string', 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
photoStrippedSize={_='photoStrippedSize', type='string', bytes='bytes'}

```


