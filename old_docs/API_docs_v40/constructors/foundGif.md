---
title: foundGif
description: Found GIF
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: foundGif  
[Back to constructors index](index.md)



Found GIF

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|GIF URL|
|thumb\_url|[string](../types/string.md) | Yes|Thumbnail URL|
|content\_url|[string](../types/string.md) | Yes|Actual URL of the content to send|
|content\_type|[string](../types/string.md) | Yes|Content-type of media|
|w|[int](../types/int.md) | Yes|Width of GIF|
|h|[int](../types/int.md) | Yes|Height of GIF|



### Type: [FoundGif](../types/FoundGif.md)


### Example:

```php
$foundGif = ['_' => 'foundGif', 'url' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'content_type' => 'string', 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
foundGif={_='foundGif', url='string', thumb_url='string', content_url='string', content_type='string', w=int, h=int}

```


