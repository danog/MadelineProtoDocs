---
title: updateWebPage
description: Update web page
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateWebPage  
[Back to constructors index](index.md)



Update web page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|webpage|[WebPage](../types/WebPage.md) | Optional|Webpage|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateWebPage = ['_' => 'updateWebPage', 'webpage' => WebPage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateWebPage", "webpage": WebPage}
```


Or, if you're into Lua:

```lua
updateWebPage={_='updateWebPage', webpage=WebPage}

```


