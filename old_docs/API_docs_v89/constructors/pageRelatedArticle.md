---
title: pageRelatedArticle
description: Related article
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageRelatedArticle  
[Back to constructors index](index.md)



Related article

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL of article|
|webpage\_id|[long](../types/long.md) | Yes|Webpage ID of generated IV preview|
|title|[string](../types/string.md) | Optional|Title|
|description|[string](../types/string.md) | Optional|Description|
|photo\_id|[long](../types/long.md) | Optional|ID of preview photo|
|author|[string](../types/string.md) | Optional|Author name|
|published\_date|[int](../types/int.md) | Optional|Date of pubblication|



### Type: [PageRelatedArticle](../types/PageRelatedArticle.md)


### Example:

```php
$pageRelatedArticle = ['_' => 'pageRelatedArticle', 'url' => 'string', 'webpage_id' => long, 'title' => 'string', 'description' => 'string', 'photo_id' => long, 'author' => 'string', 'published_date' => int];
```  


Or, if you're into Lua:

```lua
pageRelatedArticle={_='pageRelatedArticle', url='string', webpage_id=long, title='string', description='string', photo_id=long, author='string', published_date=int}

```


