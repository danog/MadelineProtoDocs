---
title: "updateBotInlineQuery"
description: "An incoming inline query"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotInlineQuery  
[Back to constructors index](/API_docs/constructors/index.md)



An incoming inline query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.md) | Yes|Query ID|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|query|[string](/API_docs/types/string.md) | Yes|Text of query|
|geo|[GeoPoint](/API_docs/types/GeoPoint.md) | Optional|Attached geolocation|
|peer\_type|[InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.md) | Optional|
|offset|[string](/API_docs/types/string.md) | Yes|Offset to navigate through results|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateBotInlineQuery = ['_' => 'updateBotInlineQuery', 'query_id' => long, 'user_id' => long, 'query' => 'string', 'geo' => GeoPoint, 'peer_type' => InlineQueryPeerType, 'offset' => 'string'];
```  
