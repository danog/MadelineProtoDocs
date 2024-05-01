---
title: "pageBlockRelatedArticles"
description: "Related articles"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockRelatedArticles  
[Back to constructors index](/API_docs/constructors/index.html)



Related articles

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[RichText](/API_docs/types/RichText.html) | Yes|Title|
|articles|Array of [PageRelatedArticle](/API_docs/types/PageRelatedArticle.html) | Yes|Related articles|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockRelatedArticles = ['_' => 'pageBlockRelatedArticles', 'title' => RichText, 'articles' => [PageRelatedArticle, PageRelatedArticle]];
```  
