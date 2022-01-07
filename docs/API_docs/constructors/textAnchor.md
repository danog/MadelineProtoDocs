---
title: "textAnchor"
description: "Text linking to another section of the page"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textAnchor  
[Back to constructors index](index.md)



Text linking to another section of the page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|name|[string](../types/string.md) | Yes|Section name|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textAnchor = ['_' => 'textAnchor', 'text' => RichText, 'name' => 'string'];
```  
