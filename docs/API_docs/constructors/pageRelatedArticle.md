---
title: "pageRelatedArticle"
description: "Related article"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageRelatedArticle  
[Back to constructors index](/API_docs/constructors/index.html)



Related article

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|URL of article|
|webpage\_id|[long](/API_docs/types/long.html) | Yes|Webpage ID of generated IV preview|
|title|[string](/API_docs/types/string.html) | Optional|Title|
|description|[string](/API_docs/types/string.html) | Optional|Description|
|photo\_id|[long](/API_docs/types/long.html) | Optional|ID of preview photo|
|author|[string](/API_docs/types/string.html) | Optional|Author name|
|published\_date|[int](/API_docs/types/int.html) | Optional|Date of publication|



### Type: [PageRelatedArticle](/API_docs/types/PageRelatedArticle.html)


### Example:

```
$pageRelatedArticle = ['_' => 'pageRelatedArticle', 'url' => 'string', 'webpage_id' => long, 'title' => 'string', 'description' => 'string', 'photo_id' => long, 'author' => 'string', 'published_date' => int];
```  
