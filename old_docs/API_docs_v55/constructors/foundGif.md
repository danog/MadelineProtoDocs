---
title: foundGif
description: Found gif
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: foundGif  
[Back to constructors index](index.md)



Found gif

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|thumb\_url|[string](../types/string.md) | Yes|Thumbnail URL|
|content\_url|[string](../types/string.md) | Yes|Content URL|
|content\_type|[string](../types/string.md) | Yes|Content type|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|



### Type: [FoundGif](../types/FoundGif.md)


### Example:

```php
$foundGif = ['_' => 'foundGif', 'url' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'content_type' => 'string', 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
foundGif={_='foundGif', url='string', thumb_url='string', content_url='string', content_type='string', w=int, h=int}

```


