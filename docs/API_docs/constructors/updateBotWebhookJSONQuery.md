---
title: "updateBotWebhookJSONQuery"
description: "A new incoming query; for bots only"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotWebhookJSONQuery  
[Back to constructors index](index.md)



A new incoming query; for bots only

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query identifier|
|data|[DataJSON](../types/DataJSON.md) | Yes|Query data|
|timeout|[int](../types/int.md) | Yes|Query timeout|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotWebhookJSONQuery = ['_' => 'updateBotWebhookJSONQuery', 'query_id' => long, 'data' => DataJSON, 'timeout' => int];
```  


Or, if you're into Lua:

```lua
updateBotWebhookJSONQuery={_='updateBotWebhookJSONQuery', query_id=long, data=DataJSON, timeout=int}

```


