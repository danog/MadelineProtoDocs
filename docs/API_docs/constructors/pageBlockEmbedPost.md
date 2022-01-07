---
title: "pageBlockEmbedPost"
description: "An embedded post"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockEmbedPost  
[Back to constructors index](index.md)



An embedded post

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|Web page URL|
|webpage\_id|[long](../types/long.md) | Yes|ID of generated webpage preview|
|author\_photo\_id|[long](../types/long.md) | Yes|ID of the author's photo|
|author|[string](../types/string.md) | Yes|Author name|
|date|[int](../types/int.md) | Yes|Creation date|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Post contents|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockEmbedPost = ['_' => 'pageBlockEmbedPost', 'url' => 'string', 'webpage_id' => long, 'author_photo_id' => long, 'author' => 'string', 'date' => int, 'blocks' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  
