---
title: "pageBlockOrderedList"
description: "Ordered list of IV blocks"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockOrderedList  
[Back to constructors index](index.md)



Ordered list of IV blocks

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageListOrderedItem](../types/PageListOrderedItem.md) | Yes|List items|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockOrderedList = ['_' => 'pageBlockOrderedList', 'items' => [PageListOrderedItem, PageListOrderedItem]];
```  


Or, if you're into Lua:

```lua
pageBlockOrderedList={_='pageBlockOrderedList', items={PageListOrderedItem}}

```


