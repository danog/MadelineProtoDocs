---
title: inputMediaGifExternal
description: New GIF animation that will be uploaded by the server using the specified URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGifExternal  
[Back to constructors index](index.md)



New GIF animation that will be uploaded by the server using the specified URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|q|[string](../types/string.md) | Yes|Query|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGifExternal = ['_' => 'inputMediaGifExternal', 'url' => 'string', 'q' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaGifExternal={_='inputMediaGifExternal', url='string', q='string'}

```


