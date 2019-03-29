---
title: pageBlockPreformatted
description: Preformatted text paragraph
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPreformatted  
[Back to constructors index](index.md)



Preformatted text paragraph

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Paragraph text|
|language|[string](../types/string.md) | Yes|Programming language for which the text should be formatted|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPreformatted = ['_' => 'pageBlockPreformatted', 'text' => RichText, 'language' => 'string'];
```  


Or, if you're into Lua:

```lua
pageBlockPreformatted={_='pageBlockPreformatted', text=RichText, language='string'}

```


