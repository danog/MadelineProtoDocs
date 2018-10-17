---
title: pageBlockPreformatted
description: pageBlockPreformatted attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPreformatted  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|
|language|[string](../types/string.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPreformatted = ['_' => 'pageBlockPreformatted', 'text' => RichText, 'language' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockPreformatted", "text": RichText, "language": "string"}
```


Or, if you're into Lua:

```lua
pageBlockPreformatted={_='pageBlockPreformatted', text=RichText, language='string'}

```


