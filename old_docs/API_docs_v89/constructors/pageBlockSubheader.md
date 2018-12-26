---
title: pageBlockSubheader
description: Page block subheader
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockSubheader  
[Back to constructors index](index.md)



Page block subheader

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockSubheader = ['_' => 'pageBlockSubheader', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockSubheader", "text": RichText}
```


Or, if you're into Lua:

```lua
pageBlockSubheader={_='pageBlockSubheader', text=RichText}

```


