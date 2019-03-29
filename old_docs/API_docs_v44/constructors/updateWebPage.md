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
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateWebPage = ['_' => 'updateWebPage', 'webpage' => WebPage, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateWebPage={_='updateWebPage', webpage=WebPage, pts=int, pts_count=int}

```


