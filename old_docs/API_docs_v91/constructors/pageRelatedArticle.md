---
title: pageRelatedArticle
description: Page related article
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageRelatedArticle  
[Back to constructors index](index.md)



Page related article

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|webpage\_id|[long](../types/long.md) | Yes|Webpage ID|
|title|[string](../types/string.md) | Optional|Title|
|description|[string](../types/string.md) | Optional|Description|
|photo\_id|[long](../types/long.md) | Optional|Photo ID|
|author|[string](../types/string.md) | Optional|Author|
|published\_date|[int](../types/int.md) | Optional|Published date|



### Type: [PageRelatedArticle](../types/PageRelatedArticle.md)


### Example:

```php
$pageRelatedArticle = ['_' => 'pageRelatedArticle', 'url' => 'string', 'webpage_id' => long, 'title' => 'string', 'description' => 'string', 'photo_id' => long, 'author' => 'string', 'published_date' => int];
```  


Or, if you're into Lua:

```lua
pageRelatedArticle={_='pageRelatedArticle', url='string', webpage_id=long, title='string', description='string', photo_id=long, author='string', published_date=int}

```


