---
title: "pageBlockPreformatted"
description: "Preformatted (<pre> text)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPreformatted  
[Back to constructors index](index.md)



Preformatted (`<pre>` text)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Text|
|language|[string](../types/string.md) | Yes|Programming language of preformatted text|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPreformatted = ['_' => 'pageBlockPreformatted', 'text' => RichText, 'language' => 'string'];
```  


Or, if you're into Lua:

```lua
pageBlockPreformatted={_='pageBlockPreformatted', text=RichText, language='string'}

```


