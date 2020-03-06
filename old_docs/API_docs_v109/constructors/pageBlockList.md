---
title: pageBlockList
description: Unordered list of IV blocks
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockList  
[Back to constructors index](index.md)



Unordered list of IV blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageListItem](../types/PageListItem.md) | Yes|Items|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockList = ['_' => 'pageBlockList', 'items' => [PageListItem, PageListItem]];
```  


Or, if you're into Lua:

```lua
pageBlockList={_='pageBlockList', items={PageListItem}}

```


