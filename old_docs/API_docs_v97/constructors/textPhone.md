---
title: textPhone
description: Text phone
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textPhone  
[Back to constructors index](index.md)



Text phone

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|phone|[string](../types/string.md) | Yes|Phone|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textPhone = ['_' => 'textPhone', 'text' => RichText, 'phone' => 'string'];
```  


Or, if you're into Lua:

```lua
textPhone={_='textPhone', text=RichText, phone='string'}

```


