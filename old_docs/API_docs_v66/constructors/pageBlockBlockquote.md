---
title: pageBlockBlockquote
description: Page block blockquote
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockBlockquote  
[Back to constructors index](index.md)



Page block blockquote

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|caption|[RichText](../types/RichText.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockBlockquote = ['_' => 'pageBlockBlockquote', 'text' => RichText, 'caption' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockBlockquote", "text": RichText, "caption": RichText}
```


Or, if you're into Lua:

```lua
pageBlockBlockquote={_='pageBlockBlockquote', text=RichText, caption=RichText}

```


