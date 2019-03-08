---
title: exportedMessageLink
description: Exported message link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: exportedMessageLink  
[Back to constructors index](index.md)



Exported message link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|link|[string](../types/string.md) | Yes|Link|
|html|[string](../types/string.md) | Yes|Html|



### Type: [ExportedMessageLink](../types/ExportedMessageLink.md)


### Example:

```php
$exportedMessageLink = ['_' => 'exportedMessageLink', 'link' => 'string', 'html' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "exportedMessageLink", "link": "string", "html": "string"}
```


Or, if you're into Lua:

```lua
exportedMessageLink={_='exportedMessageLink', link='string', html='string'}

```


