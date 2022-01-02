---
title: "messageMediaWebPage"
description: "Preview of webpage"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaWebPage  
[Back to constructors index](index.md)



Preview of webpage

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|webpage|[WebPage](../types/WebPage.md) | Optional|Webpage preview|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaWebPage = ['_' => 'messageMediaWebPage', 'webpage' => WebPage];
```  


Or, if you're into Lua:

```lua
messageMediaWebPage={_='messageMediaWebPage', webpage=WebPage}

```


