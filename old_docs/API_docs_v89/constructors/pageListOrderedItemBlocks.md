---
title: pageListOrderedItemBlocks
description: Page list ordered item blocks
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageListOrderedItemBlocks  
[Back to constructors index](index.md)



Page list ordered item blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|num|[string](../types/string.md) | Yes|Num|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|



### Type: [PageListOrderedItem](../types/PageListOrderedItem.md)


### Example:

```php
$pageListOrderedItemBlocks = ['_' => 'pageListOrderedItemBlocks', 'num' => 'string', 'blocks' => [PageBlock, PageBlock]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageListOrderedItemBlocks", "num": "string", "blocks": [PageBlock]}
```


Or, if you're into Lua:

```lua
pageListOrderedItemBlocks={_='pageListOrderedItemBlocks', num='string', blocks={PageBlock}}

```


