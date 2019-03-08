---
title: pageBlockSubtitle
description: Page block subtitle
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockSubtitle  
[Back to constructors index](index.md)



Page block subtitle

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockSubtitle = ['_' => 'pageBlockSubtitle', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockSubtitle", "text": RichText}
```


Or, if you're into Lua:

```lua
pageBlockSubtitle={_='pageBlockSubtitle', text=RichText}

```


