---
title: "pageListOrderedItemBlocks"
description: "Ordered list of IV blocks"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageListOrderedItemBlocks  
[Back to constructors index](/API_docs/constructors/index.html)



Ordered list of [IV](https://instantview.telegram.org) blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|num|[string](/API_docs/types/string.html) | Yes|Number of element within ordered list|
|blocks|Array of [PageBlock](/API_docs/types/PageBlock.html) | Yes|Item contents|



### Type: [PageListOrderedItem](/API_docs/types/PageListOrderedItem.html)


### Example:

```
$pageListOrderedItemBlocks = ['_' => 'pageListOrderedItemBlocks', 'num' => 'string', 'blocks' => [PageBlock, PageBlock]];
```  
