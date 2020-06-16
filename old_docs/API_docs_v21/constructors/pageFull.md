---
title: pageFull
description: pageFull attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageFull  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|
|photos|Array of [Photo](../types/Photo.md) | Yes|
|documents|Array of [Document](../types/Document.md) | Yes|



### Type: [Page](../types/Page.md)


### Example:

```php
$pageFull = ['_' => 'pageFull', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
pageFull={_='pageFull', blocks={PageBlock}, photos={Photo}, documents={Document}}

```


