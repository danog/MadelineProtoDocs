---
title: pageBlockOrderedList
description: Page block ordered list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockOrderedList  
[Back to constructors index](index.md)



Page block ordered list

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageListOrderedItem](../types/PageListOrderedItem.md) | Yes|Items|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockOrderedList = ['_' => 'pageBlockOrderedList', 'items' => [PageListOrderedItem, PageListOrderedItem]];
```  


Or, if you're into Lua:

```lua
pageBlockOrderedList={_='pageBlockOrderedList', items={PageListOrderedItem}}

```


