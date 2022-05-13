---
title: "pageBlockList"
description: "Unordered list of IV blocks"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockList  
[Back to constructors index](/API_docs/constructors/index.html)



Unordered list of IV blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageListItem](/API_docs/types/PageListItem.html) | Yes|List of blocks in an IV page|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockList = ['_' => 'pageBlockList', 'items' => [PageListItem, PageListItem]];
```  
