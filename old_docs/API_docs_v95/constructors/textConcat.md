---
title: textConcat
description: Text concat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textConcat  
[Back to constructors index](index.md)



Text concat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|texts|Array of [RichText](../types/RichText.md) | Yes|Texts|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textConcat = ['_' => 'textConcat', 'texts' => [RichText, RichText]];
```  


Or, if you're into Lua:

```lua
textConcat={_='textConcat', texts={RichText}}

```


