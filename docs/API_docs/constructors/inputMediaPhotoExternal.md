---
title: "inputMediaPhotoExternal"
description: "New photo that will be uploaded by the server using the specified URL"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPhotoExternal  
[Back to constructors index](index.md)



New photo that will be uploaded by the server using the specified URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL of the photo|
|ttl\_seconds|[int](../types/int.md) | Optional|Self-destruct time to live of photo|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPhotoExternal = ['_' => 'inputMediaPhotoExternal', 'url' => 'string', 'ttl_seconds' => int];
```  


Or, if you're into Lua:

```lua
inputMediaPhotoExternal={_='inputMediaPhotoExternal', url='string', ttl_seconds=int}

```


