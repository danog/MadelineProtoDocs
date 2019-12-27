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
|url|[string](../types/string.md) | Yes|Original page HTTP URL|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|documents|Array of [Document](../types/Document.md) | Yes|Documents|



### Type: [Page](../types/Page.md)


### Example:

```php
$page = ['_' => 'page', 'part' => Bool, 'rtl' => Bool, 'url' => 'string', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
page={_='page', part=Bool, rtl=Bool, url='string', blocks={PageBlock}, photos={Photo}, documents={Document}}

```


