---
title: "pageBlockCollage"
description: "Collage of media"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockCollage  
[Back to constructors index](/API_docs/constructors/index.md)



Collage of media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageBlock](/API_docs/types/PageBlock.md) | Yes|Media elements|
|caption|[PageCaption](/API_docs/types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockCollage = ['_' => 'pageBlockCollage', 'items' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  
