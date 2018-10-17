---
title: updateBotWebhookJSONQuery
description: updateBotWebhookJSONQuery attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotWebhookJSONQuery  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](../types/long.md) | Yes|
|data|[DataJSON](../types/DataJSON.md) | Yes|
|timeout|[int](../types/int.md) | Yes|



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


