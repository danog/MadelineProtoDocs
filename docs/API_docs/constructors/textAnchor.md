---
title: textAnchor
description: Text anchor
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textAnchor  
[Back to constructors index](index.md)



Text anchor

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|name|[string](../types/string.md) | Yes|Name|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textAnchor = ['_' => 'textAnchor', 'text' => RichText, 'name' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "textAnchor", "text": RichText, "name": "string"}
```


Or, if you're into Lua:

```lua
textAnchor={_='textAnchor', text=RichText, name='string'}

```


