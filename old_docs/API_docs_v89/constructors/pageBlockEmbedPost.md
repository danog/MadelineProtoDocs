---
title: pageBlockEmbedPost
description: Page block embed post
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockEmbedPost  
[Back to constructors index](index.md)



Page block embed post

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|webpage\_id|[long](../types/long.md) | Yes|Webpage ID|
|author\_photo\_id|[long](../types/long.md) | Yes|Author photo ID|
|author|[string](../types/string.md) | Yes|Author|
|date|[int](../types/int.md) | Yes|Date|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockEmbedPost = ['_' => 'pageBlockEmbedPost', 'url' => 'string', 'webpage_id' => long, 'author_photo_id' => long, 'author' => 'string', 'date' => int, 'blocks' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockEmbedPost", "url": "string", "webpage_id": long, "author_photo_id": long, "author": "string", "date": int, "blocks": [PageBlock], "caption": PageCaption}
```


Or, if you're into Lua:

```lua
pageBlockEmbedPost={_='pageBlockEmbedPost', url='string', webpage_id=long, author_photo_id=long, author='string', date=int, blocks={PageBlock}, caption=PageCaption}

```


