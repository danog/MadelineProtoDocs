---
title: "pageBlockEmbed"
description: "An embedded webpage"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockEmbed  
[Back to constructors index](/API_docs/constructors/index.html)



An embedded webpage

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_width|[Bool](/API_docs/types/Bool.html) | Optional|Whether the block should be full width|
|allow\_scrolling|[Bool](/API_docs/types/Bool.html) | Optional|Whether scrolling should be allowed|
|url|[string](/API_docs/types/string.html) | Optional|Web page URL, if available|
|html|[string](/API_docs/types/string.html) | Optional|HTML-markup of the embedded page|
|poster\_photo\_id|[long](/API_docs/types/long.html) | Optional|Poster photo, if available|
|w|[int](/API_docs/types/int.html) | Optional|Block width, if known|
|h|[int](/API_docs/types/int.html) | Optional|Block height, if known|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockEmbed = ['_' => 'pageBlockEmbed', 'full_width' => Bool, 'allow_scrolling' => Bool, 'url' => 'string', 'html' => 'string', 'poster_photo_id' => long, 'w' => int, 'h' => int, 'caption' => PageCaption];
```  
