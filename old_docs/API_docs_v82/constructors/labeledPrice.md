---
title: labeledPrice
description: Labeled price
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: labeledPrice  
[Back to constructors index](index.md)



Labeled price

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|label|[string](../types/string.md) | Yes|Label|
|amount|[long](../types/long.md) | Yes|Amount|



### Type: [LabeledPrice](../types/LabeledPrice.md)


### Example:

```php
$labeledPrice = ['_' => 'labeledPrice', 'label' => 'string', 'amount' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "labeledPrice", "label": "string", "amount": long}
```


Or, if you're into Lua:

```lua
labeledPrice={_='labeledPrice', label='string', amount=long}

```


