---
title: keyboardButtonUrl
description: keyboardButtonUrl attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: keyboardButtonUrl  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[string](../types/string.md) | Yes|
|url|[string](../types/string.md) | Yes|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```
$keyboardButtonUrl = ['_' => 'keyboardButtonUrl', 'text' => 'string', 'url' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "keyboardButtonUrl", "text": "string", "url": "string"}
```


Or, if you're into Lua:  


```
keyboardButtonUrl={_='keyboardButtonUrl', text='string', url='string'}

```


