---
title: pageBlockParagraph
description: pageBlockParagraph attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockParagraph  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockParagraph = ['_' => 'pageBlockParagraph', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockParagraph", "text": RichText}
```


Or, if you're into Lua:

```lua
pageBlockParagraph={_='pageBlockParagraph', text=RichText}

```


