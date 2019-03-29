---
title: pagePart
description: Page part
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pagePart  
[Back to constructors index](index.md)



Page part

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|documents|Array of [Document](../types/Document.md) | Yes|Documents|



### Type: [Page](../types/Page.md)


### Example:

```php
$pagePart = ['_' => 'pagePart', 'blocks' => [PageBlock, PageBlock], 'photos' => [Photo, Photo], 'documents' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
pagePart={_='pagePart', blocks={PageBlock}, photos={Photo}, documents={Document}}

```


