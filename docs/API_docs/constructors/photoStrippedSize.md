---
title: photoStrippedSize
description: Just the image's content
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoStrippedSize  
[Back to constructors index](index.html)



Just the image's content

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.html) | Yes|Thumbnail type|
|bytes|[bytes](../types/bytes.html) | Yes|Thumbnail data|
|inflated|[bytes](../types/bytes.html) | Yes|JPG image data|



### Type: [PhotoSize](../types/PhotoSize.html)


### Example:

```php
$photoStrippedSize = ['_' => 'photoStrippedSize', 'type' => 'string', 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
photoStrippedSize={_='photoStrippedSize', type='string', bytes='bytes'}

```


