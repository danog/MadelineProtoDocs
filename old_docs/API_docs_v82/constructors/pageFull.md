---
title: pageFull
description: Page full
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageFull  
[Back to constructors index](index.md)



Page full

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|documents|Array of [Document](../types/Document.md) | Yes|Documents|



### Type: [Page](../types/Page.md)


### Example:

```php
$pageFull = ['_' => 'pageFull', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
pageFull={_='pageFull', blocks={PageBlock}, photos={Photo}, documents={Document}}

```


