---
title: "textEmail"
description: "Rich text email link"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textEmail  
[Back to constructors index](index.md)



Rich text email link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Link text|
|email|[string](../types/string.md) | Yes|Email address|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textEmail = ['_' => 'textEmail', 'text' => RichText, 'email' => 'string'];
```  
