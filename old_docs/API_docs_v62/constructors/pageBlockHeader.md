---
title: pageBlockHeader
description: pageBlockHeader attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockHeader  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockHeader = ['_' => 'pageBlockHeader', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockHeader", "text": RichText}
```


Or, if you're into Lua:

```lua
pageBlockHeader={_='pageBlockHeader', text=RichText}

```


