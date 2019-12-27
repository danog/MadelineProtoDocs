---
title: updateWebPage
description: An [instant view](https://instantview.telegram.org) webpage preview was generated
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateWebPage  
[Back to constructors index](index.md)



An [instant view](https://instantview.telegram.org) webpage preview was generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|webpage|[WebPage](../types/WebPage.md) | Optional|Webpage preview|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateWebPage = ['_' => 'updateWebPage', 'webpage' => WebPage];
```  


Or, if you're into Lua:

```lua
updateWebPage={_='updateWebPage', webpage=WebPage}

```


