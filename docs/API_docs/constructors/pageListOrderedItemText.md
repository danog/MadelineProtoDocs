---
title: "pageListOrderedItemText"
description: "Ordered list of text items"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageListOrderedItemText  
[Back to constructors index](index.md)



Ordered list of text items

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|num|[string](../types/string.md) | Yes|Number of element within ordered list|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [PageListOrderedItem](../types/PageListOrderedItem.md)


### Example:

```php
$pageListOrderedItemText = ['_' => 'pageListOrderedItemText', 'num' => 'string', 'text' => RichText];
```  


Or, if you're into Lua:

```lua
pageListOrderedItemText={_='pageListOrderedItemText', num='string', text=RichText}

```


