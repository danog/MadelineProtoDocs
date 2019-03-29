---
title: textEmail
description: Text email
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textEmail  
[Back to constructors index](index.md)



Text email

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|email|[string](../types/string.md) | Yes|Email|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textEmail = ['_' => 'textEmail', 'text' => RichText, 'email' => 'string'];
```  


Or, if you're into Lua:

```lua
textEmail={_='textEmail', text=RichText, email='string'}

```


