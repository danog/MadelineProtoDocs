---
title: textEmail
description: textEmail attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textEmail  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|
|email|[string](../types/string.md) | Yes|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textEmail = ['_' => 'textEmail', 'text' => RichText, 'email' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "textEmail", "text": RichText, "email": "string"}
```


Or, if you're into Lua:

```lua
textEmail={_='textEmail', text=RichText, email='string'}

```


