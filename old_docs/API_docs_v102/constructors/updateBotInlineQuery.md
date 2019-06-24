---
title: updateBotInlineQuery
description: Update bot inline query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotInlineQuery  
[Back to constructors index](index.md)



Update bot inline query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|query|[string](../types/string.md) | Yes|Query|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|
|offset|[string](../types/string.md) | Yes|Offset|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotInlineQuery = ['_' => 'updateBotInlineQuery', 'query_id' => long, 'user_id' => int, 'query' => 'string', 'geo' => GeoPoint, 'offset' => 'string'];
```  


Or, if you're into Lua:

```lua
updateBotInlineQuery={_='updateBotInlineQuery', query_id=long, user_id=int, query='string', geo=GeoPoint, offset='string'}

```


