---
title: pageBlockPullquote
description: pageBlockPullquote attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPullquote  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|
|caption|[RichText](../types/RichText.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPullquote = ['_' => 'pageBlockPullquote', 'text' => RichText, 'caption' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockPullquote", "text": RichText, "caption": RichText}
```


Or, if you're into Lua:

```lua
pageBlockPullquote={_='pageBlockPullquote', text=RichText, caption=RichText}

```


