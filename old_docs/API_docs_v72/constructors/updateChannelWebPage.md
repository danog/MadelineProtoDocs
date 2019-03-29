---
title: updateChannelWebPage
description: Update channel web page
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelWebPage  
[Back to constructors index](index.md)



Update channel web page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|webpage|[WebPage](../types/WebPage.md) | Optional|Webpage|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelWebPage = ['_' => 'updateChannelWebPage', 'channel_id' => int, 'webpage' => WebPage, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateChannelWebPage={_='updateChannelWebPage', channel_id=int, webpage=WebPage, pts=int, pts_count=int}

```


