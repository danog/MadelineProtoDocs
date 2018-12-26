---
title: pageBlockList
description: Page block list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockList  
[Back to constructors index](index.md)



Page block list

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ordered|[Bool](../types/Bool.md) | Yes|Ordered?|
|items|Array of [RichText](../types/RichText.md) | Yes|Items|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockList = ['_' => 'pageBlockList', 'ordered' => Bool, 'items' => [RichText, RichText]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockList", "ordered": Bool, "items": [RichText]}
```


Or, if you're into Lua:

```lua
pageBlockList={_='pageBlockList', ordered=Bool, items={RichText}}

```


