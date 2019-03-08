---
title: textSuperscript
description: Text superscript
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textSuperscript  
[Back to constructors index](index.md)



Text superscript

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textSuperscript = ['_' => 'textSuperscript', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "textSuperscript", "text": RichText}
```


Or, if you're into Lua:

```lua
textSuperscript={_='textSuperscript', text=RichText}

```


