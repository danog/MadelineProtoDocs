---
title: pageListOrderedItemText
description: Page list ordered item text
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageListOrderedItemText  
[Back to constructors index](index.md)



Page list ordered item text

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|num|[string](../types/string.md) | Yes|Num|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [PageListOrderedItem](../types/PageListOrderedItem.md)


### Example:

```php
$pageListOrderedItemText = ['_' => 'pageListOrderedItemText', 'num' => 'string', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageListOrderedItemText", "num": "string", "text": RichText}
```


Or, if you're into Lua:

```lua
pageListOrderedItemText={_='pageListOrderedItemText', num='string', text=RichText}

```


