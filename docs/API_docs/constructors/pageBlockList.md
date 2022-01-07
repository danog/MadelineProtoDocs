---
title: "pageBlockList"
description: "Unordered list of IV blocks"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockList  
[Back to constructors index](/API_docs/constructors/index.md)



Unordered list of IV blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageListItem](/API_docs/types/PageListItem.md) | Yes|List of blocks in an IV page|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockList = ['_' => 'pageBlockList', 'items' => [PageListItem, PageListItem]];
```  
