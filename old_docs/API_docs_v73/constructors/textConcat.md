---
title: textConcat
description: textConcat attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textConcat  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|texts|Array of [RichText](../types/RichText.md) | Yes|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textConcat = ['_' => 'textConcat', 'texts' => [RichText, RichText]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "textConcat", "texts": [RichText]}
```


Or, if you're into Lua:

```lua
textConcat={_='textConcat', texts={RichText}}

```


