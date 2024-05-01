---
title: "pageBlockAuthorDate"
description: "Author and date of creation of article"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAuthorDate  
[Back to constructors index](/API_docs/constructors/index.html)



Author and date of creation of article

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|author|[RichText](/API_docs/types/RichText.html) | Yes|Author name|
|published\_date|[int](/API_docs/types/int.html) | Yes|Date of publication|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockAuthorDate = ['_' => 'pageBlockAuthorDate', 'author' => RichText, 'published_date' => int];
```  
