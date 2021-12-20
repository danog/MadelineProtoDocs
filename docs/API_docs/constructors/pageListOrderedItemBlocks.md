---
title: "pageListOrderedItemBlocks"
description: "Ordered list of IV blocks"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageListOrderedItemBlocks  
[Back to constructors index](index.md)



Ordered list of [IV](https://instantview.telegram.org) blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|num|[string](../types/string.md) | Yes|Number of element within ordered list|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Item contents|



### Type: [PageListOrderedItem](../types/PageListOrderedItem.md)


### Example:

```php
$pageListOrderedItemBlocks = ['_' => 'pageListOrderedItemBlocks', 'num' => 'string', 'blocks' => [PageBlock, PageBlock]];
```  


Or, if you're into Lua:

```lua
pageListOrderedItemBlocks={_='pageListOrderedItemBlocks', num='string', blocks={PageBlock}}

```


