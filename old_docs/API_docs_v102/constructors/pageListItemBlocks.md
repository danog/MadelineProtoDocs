---
title: pageListItemBlocks
description: Page list item blocks
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageListItemBlocks  
[Back to constructors index](index.md)



Page list item blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|



### Type: [PageListItem](../types/PageListItem.md)


### Example:

```php
$pageListItemBlocks = ['_' => 'pageListItemBlocks', 'blocks' => [PageBlock, PageBlock]];
```  


Or, if you're into Lua:

```lua
pageListItemBlocks={_='pageListItemBlocks', blocks={PageBlock}}

```


