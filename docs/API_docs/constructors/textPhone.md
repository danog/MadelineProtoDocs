---
title: "textPhone"
description: "Rich text linked to a phone number"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textPhone  
[Back to constructors index](index.md)



Rich text linked to a phone number

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|phone|[string](../types/string.md) | Yes|Phone number|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textPhone = ['_' => 'textPhone', 'text' => RichText, 'phone' => 'string'];
```  
