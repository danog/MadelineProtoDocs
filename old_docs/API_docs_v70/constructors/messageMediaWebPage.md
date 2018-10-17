---
title: messageMediaWebPage
description: messageMediaWebPage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaWebPage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|webpage|[WebPage](../types/WebPage.md) | Optional|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaWebPage = ['_' => 'messageMediaWebPage', 'webpage' => WebPage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaWebPage", "webpage": WebPage}
```


Or, if you're into Lua:

```lua
messageMediaWebPage={_='messageMediaWebPage', webpage=WebPage}

```


