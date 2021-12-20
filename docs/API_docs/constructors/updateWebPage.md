---
title: "updateWebPage"
description: "An instant view webpage preview was generated"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateWebPage  
[Back to constructors index](index.md)



An [instant view](https://instantview.telegram.org) webpage preview was generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|webpage|[WebPage](../types/WebPage.md) | Optional|Webpage preview|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateWebPage = ['_' => 'updateWebPage', 'webpage' => WebPage, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateWebPage={_='updateWebPage', webpage=WebPage, pts=int, pts_count=int}

```


