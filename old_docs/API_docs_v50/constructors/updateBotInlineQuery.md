---
title: updateBotInlineQuery
description: An incoming inline query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotInlineQuery  
[Back to constructors index](index.md)



An incoming inline query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[long](../types/long.md) | Yes|
|query|[string](../types/string.md) | Yes|Text of query|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Attached geolocation|
|peer\_type|[InlineQueryPeerType](../types/InlineQueryPeerType.md) | Optional|
|offset|[string](../types/string.md) | Yes|Offset to navigate through results|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotInlineQuery = ['_' => 'updateBotInlineQuery', 'query_id' => long, 'user_id' => long, 'query' => 'string', 'geo' => GeoPoint, 'peer_type' => InlineQueryPeerType, 'offset' => 'string'];
```  


Or, if you're into Lua:

```lua
updateBotInlineQuery={_='updateBotInlineQuery', query_id=long, user_id=long, query='string', geo=GeoPoint, peer_type=InlineQueryPeerType, offset='string'}

```


