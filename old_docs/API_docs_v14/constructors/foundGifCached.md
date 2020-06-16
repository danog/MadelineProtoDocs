---
title: foundGifCached
description: Found cached results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: foundGifCached  
[Back to constructors index](index.md)



Found cached results

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|GIF URL|
|photo|[Photo](../types/Photo.md) | Optional|Thumbnail|
|document|[Document](../types/Document.md) | Optional|Actual GIF document to send|



### Type: [FoundGif](../types/FoundGif.md)


### Example:

```php
$foundGifCached = ['_' => 'foundGifCached', 'url' => 'string', 'photo' => Photo, 'document' => Document];
```  


Or, if you're into Lua:

```lua
foundGifCached={_='foundGifCached', url='string', photo=Photo, document=Document}

```


