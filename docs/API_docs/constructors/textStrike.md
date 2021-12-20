---
title: "textStrike"
description: "Strikethrough text"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textStrike  
[Back to constructors index](index.md)



<del>Strikethrough</del> text

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textStrike = ['_' => 'textStrike', 'text' => RichText];
```  


Or, if you're into Lua:

```lua
textStrike={_='textStrike', text=RichText}

```


