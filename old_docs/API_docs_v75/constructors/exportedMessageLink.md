---
title: exportedMessageLink
description: Link to a message in a supergroup/channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: exportedMessageLink  
[Back to constructors index](index.md)



Link to a message in a supergroup/channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|link|[string](../types/string.md) | Yes|URL|
|html|[string](../types/string.md) | Yes|Embed code|



### Type: [ExportedMessageLink](../types/ExportedMessageLink.md)


### Example:

```php
$exportedMessageLink = ['_' => 'exportedMessageLink', 'link' => 'string', 'html' => 'string'];
```  


Or, if you're into Lua:

```lua
exportedMessageLink={_='exportedMessageLink', link='string', html='string'}

```


