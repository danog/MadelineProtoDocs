---
title: "pageRelatedArticle"
description: "Related article"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageRelatedArticle  
[Back to constructors index](/API_docs/constructors/index.md)



Related article

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.md) | Yes|URL of article|
|webpage\_id|[long](/API_docs/types/long.md) | Yes|Webpage ID of generated IV preview|
|title|[string](/API_docs/types/string.md) | Optional|Title|
|description|[string](/API_docs/types/string.md) | Optional|Description|
|photo\_id|[long](/API_docs/types/long.md) | Optional|ID of preview photo|
|author|[string](/API_docs/types/string.md) | Optional|Author name|
|published\_date|[int](/API_docs/types/int.md) | Optional|Date of pubblication|



### Type: [PageRelatedArticle](/API_docs/types/PageRelatedArticle.md)


### Example:

```php
$pageRelatedArticle = ['_' => 'pageRelatedArticle', 'url' => 'string', 'webpage_id' => long, 'title' => 'string', 'description' => 'string', 'photo_id' => long, 'author' => 'string', 'published_date' => int];
```  
