---
title: pageBlockPreformatted
description: Page block preformatted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPreformatted  
[Back to constructors index](index.md)



Page block preformatted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|language|[string](../types/string.md) | Yes|Language|



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


