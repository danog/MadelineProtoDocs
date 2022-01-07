---
title: "updateBotWebhookJSONQuery"
description: "A new incoming query; for bots only"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotWebhookJSONQuery  
[Back to constructors index](/API_docs/constructors/index.md)



A new incoming query; for bots only

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.md) | Yes|Query identifier|
|data|[DataJSON](/API_docs/types/DataJSON.md) | Yes|Query data|
|timeout|[int](/API_docs/types/int.md) | Yes|Query timeout|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateBotWebhookJSONQuery = ['_' => 'updateBotWebhookJSONQuery', 'query_id' => long, 'data' => DataJSON, 'timeout' => int];
```  
