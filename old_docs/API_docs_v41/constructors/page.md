---
title: page
description: [Instant view](https://instantview.telegram.org) page
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: page  
[Back to constructors index](index.md)



[Instant view](https://instantview.telegram.org) page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|part|[Bool](../types/Bool.md) | Optional|Indicates that not full page preview is available to the client and it will need to fetch full Instant View from the server using [messages.getWebPagePreview](../methods/messages.getWebPagePreview.md).|
|rtl|[Bool](../types/Bool.md) | Optional|Whether the page contains RTL text|
|v2|[Bool](../types/Bool.md) | Optional|Whether this is an [IV v2](https://instantview.telegram.org/docs#what-39s-new-in-2-0) page|
|url|[string](../types/string.md) | Yes|Original page HTTP URL|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Page elements (like with HTML elements, only as TL constructors)|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos in page|
|documents|Array of [Document](../types/Document.md) | Yes|Media in page|
|views|[int](../types/int.md) | Optional|Viewcount|



### Type: [Page](../types/Page.md)


### Example:

```php
$page = ['_' => 'page', 'part' => Bool, 'rtl' => Bool, 'v2' => Bool, 'url' => 'string', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document], 'views' => int];
```  


Or, if you're into Lua:

```lua
page={_='page', part=Bool, rtl=Bool, v2=Bool, url='string', blocks={PageBlock}, photos={Photo}, documents={Document}, views=int}

```


