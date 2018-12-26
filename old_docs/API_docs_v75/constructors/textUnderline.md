---
title: textUnderline
description: Text underline
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textUnderline  
[Back to constructors index](index.md)



Text underline

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textUnderline = ['_' => 'textUnderline', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "textUnderline", "text": RichText}
```


Or, if you're into Lua:

```lua
textUnderline={_='textUnderline', text=RichText}

```


