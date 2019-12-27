---
title: inputMediaPhotoExternal
description: New photo that will be uploaded by the server using the specified URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPhotoExternal  
[Back to constructors index](index.md)



New photo that will be uploaded by the server using the specified URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL of the photo|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPhotoExternal = ['_' => 'inputMediaPhotoExternal', 'url' => 'string', 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaPhotoExternal={_='inputMediaPhotoExternal', url='string', caption='string'}

```


