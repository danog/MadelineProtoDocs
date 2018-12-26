---
title: pageFull
description: Page full
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageFull  
[Back to constructors index](index.md)



Page full

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|videos|Array of [Document](../types/Document.md) | Yes|Videos|



### Type: [Page](../types/Page.md)


### Example:

```php
$pageFull = ['_' => 'pageFull', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'videos' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageFull", "blocks": [PageBlock], "photos": [Photo], "videos": [Document]}
```


Or, if you're into Lua:

```lua
pageFull={_='pageFull', blocks={PageBlock}, photos={Photo}, videos={Document}}

```


