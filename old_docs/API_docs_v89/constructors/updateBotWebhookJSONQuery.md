---
title: updateBotWebhookJSONQuery
description: Update bot webhook json query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotWebhookJSONQuery  
[Back to constructors index](index.md)



Update bot webhook json query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|data|[DataJSON](../types/DataJSON.md) | Yes|Data|
|timeout|[int](../types/int.md) | Yes|Timeout|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotWebhookJSONQuery = ['_' => 'updateBotWebhookJSONQuery', 'query_id' => long, 'data' => DataJSON, 'timeout' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateBotWebhookJSONQuery", "query_id": long, "data": DataJSON, "timeout": int}
```


Or, if you're into Lua:

```lua
updateBotWebhookJSONQuery={_='updateBotWebhookJSONQuery', query_id=long, data=DataJSON, timeout=int}

```


