---
title: "bots.answerWebhookJSONQuery"
description: "Answers a custom query; for bots only"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_answerWebhookJSONQuery.html
---
# Method: bots.answerWebhookJSONQuery
[Back to methods index](index.md)



Answers a custom query; for bots only

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|query\_id|[long](/API_docs/types/long.md) | Identifier of a custom query | Yes|
|data|[DataJSON](/API_docs/types/DataJSON.md) | JSON-serialized answer to the query | Yes|


### Return type: [Bool](/API_docs/types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->bots->answerWebhookJSONQuery(['query_id' => long, 'data' => DataJSON, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|QUERY_ID_INVALID|The query ID is invalid|
|400|USER_BOT_INVALID|This method can only be called by a bot|
|403|USER_BOT_INVALID|This method can only be called by a bot|


