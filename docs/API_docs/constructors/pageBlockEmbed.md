---
title: "pageBlockEmbed"
description: "An embedded webpage"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockEmbed  
[Back to constructors index](index.md)



An embedded webpage

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_width|[Bool](../types/Bool.md) | Optional|Whether the block should be full width|
|allow\_scrolling|[Bool](../types/Bool.md) | Optional|Whether scrolling should be allowed|
|url|[string](../types/string.md) | Optional|Web page URL, if available|
|html|[string](../types/string.md) | Optional|HTML-markup of the embedded page|
|poster\_photo\_id|[long](../types/long.md) | Optional|Poster photo, if available|
|w|[int](../types/int.md) | Optional|Block width, if known|
|h|[int](../types/int.md) | Optional|Block height, if known|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockEmbed = ['_' => 'pageBlockEmbed', 'full_width' => Bool, 'allow_scrolling' => Bool, 'url' => 'string', 'html' => 'string', 'poster_photo_id' => long, 'w' => int, 'h' => int, 'caption' => PageCaption];
```  
