---
title: "pageBlockSlideshow"
description: "Slideshow"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockSlideshow  
[Back to constructors index](index.md)



Slideshow

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageBlock](../types/PageBlock.md) | Yes|Slideshow items|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockSlideshow = ['_' => 'pageBlockSlideshow', 'items' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  
