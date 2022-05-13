---
title: "updateBotInlineQuery"
description: "An incoming inline query"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotInlineQuery  
[Back to constructors index](/API_docs/constructors/index.html)



An incoming inline query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Query ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|User that sent the query|
|query|[string](/API_docs/types/string.html) | Yes|Text of query|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Attached geolocation|
|peer\_type|[InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html) | Optional|Type of the chat from which the inline query was sent.|
|offset|[string](/API_docs/types/string.html) | Yes|Offset to navigate through results|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotInlineQuery = ['_' => 'updateBotInlineQuery', 'query_id' => long, 'user_id' => long, 'query' => 'string', 'geo' => GeoPoint, 'peer_type' => InlineQueryPeerType, 'offset' => 'string'];
```  
