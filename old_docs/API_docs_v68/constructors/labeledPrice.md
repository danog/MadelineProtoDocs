---
title: labeledPrice
description: labeledPrice attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: labeledPrice  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|label|[string](../types/string.md) | Yes|
|amount|[long](../types/long.md) | Yes|



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


