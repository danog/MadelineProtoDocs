---
title: "pageBlockSlideshow"
description: "Slideshow"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockSlideshow  
[Back to constructors index](/API_docs/constructors/index.html)



Slideshow

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|Slideshow items|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockSlideshow = ['_' => 'pageBlockSlideshow', 'items' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  
