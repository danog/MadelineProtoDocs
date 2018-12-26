---
title: page
description: Page
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: page  
[Back to constructors index](index.md)



Page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|part|[Bool](../types/Bool.md) | Optional|Part?|
|rtl|[Bool](../types/Bool.md) | Optional|Rtl?|
|url|[string](../types/string.md) | Yes|URL|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|documents|Array of [Document](../types/Document.md) | Yes|Documents|



### Type: [Page](../types/Page.md)


### Example:

```php
$page = ['_' => 'page', 'part' => Bool, 'rtl' => Bool, 'url' => 'string', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "page", "part": Bool, "rtl": Bool, "url": "string", "blocks": [PageBlock], "photos": [Photo], "documents": [Document]}
```


Or, if you're into Lua:

```lua
page={_='page', part=Bool, rtl=Bool, url='string', blocks={PageBlock}, photos={Photo}, documents={Document}}

```


