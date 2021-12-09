---
title: photoPathSize
description: Messages with animated stickers can have a compressed svg (&lt; 300 bytes) to show the outline of the sticker before fetching the actual lottie animation.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoPathSize  
[Back to constructors index](index.md)



Messages with animated stickers can have a compressed svg (&lt; 300 bytes) to show the outline of the sticker before fetching the actual lottie animation.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Always `j`|
|bytes|[bytes](../types/bytes.md) | Yes|Compressed SVG path payload, [see here for decompression instructions](https://core.telegram.org/api/files#vector-thumbnails)|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoPathSize = ['_' => 'photoPathSize', 'type' => 'string', 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
photoPathSize={_='photoPathSize', type='string', bytes='bytes'}

```


