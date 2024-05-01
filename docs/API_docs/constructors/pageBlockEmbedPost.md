---
title: "pageBlockEmbedPost"
description: "An embedded post"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockEmbedPost  
[Back to constructors index](/API_docs/constructors/index.html)



An embedded post

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|Web page URL|
|webpage\_id|[long](/API_docs/types/long.html) | Yes|ID of generated webpage preview|
|author\_photo\_id|[long](/API_docs/types/long.html) | Yes|ID of the author's photo|
|author|[string](/API_docs/types/string.html) | Yes|Author name|
|date|[int](/API_docs/types/int.html) | Yes|Creation date|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|Post contents|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockEmbedPost = ['_' => 'pageBlockEmbedPost', 'url' => 'string', 'webpage_id' => long, 'author_photo_id' => long, 'author' => 'string', 'date' => int, 'blocks' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  
