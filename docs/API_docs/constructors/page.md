---
title: "page"
description: "Instant view page"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: page  
[Back to constructors index](/API_docs/constructors/index.html)



[Instant view](https://instantview.telegram.org) page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|part|[Bool](/API_docs/types/Bool.html) | Optional|Indicates that not full page preview is available to the client and it will need to fetch full Instant View from the server using [messages.getWebPagePreview](../methods/messages.getWebPagePreview.html).|
|rtl|[Bool](/API_docs/types/Bool.html) | Optional|Whether the page contains RTL text|
|v2|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is an [IV v2](https://instantview.telegram.org/docs#what-39s-new-in-2-0) page|
|url|[string](/API_docs/types/string.html) | Yes|Original page HTTP URL|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|Page elements (like with HTML elements, only as TL constructors)|
|photos|Array of [Photo](/API_docs/types/Photo.html) | Yes|Photos in page|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|Media in page|
|views|[int](/API_docs/types/int.html) | Optional|View count|



### Type: [Page](/API_docs/types/Page.html)


### Example:

```
$page = ['_' => 'page', 'part' => Bool, 'rtl' => Bool, 'v2' => Bool, 'url' => 'string', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document], 'views' => int];
```  
