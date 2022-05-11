---
title: "messages.setBotCallbackAnswer"
description: "Set the callback answer to a user button press (bots only)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setBotCallbackAnswer.html
---
# Method: messages.setBotCallbackAnswer
[Back to methods index](index.html)



Set the callback answer to a user button press (bots only)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|alert|[Bool](/API_docs/types/Bool.html) | Whether to show the message as a popup instead of a toast notification | Optional|
|query\_id|[long](/API_docs/types/long.html) | Query ID | Yes|
|message|[string](/API_docs/types/string.html) | Popup to show | Optional|
|url|[string](/API_docs/types/string.html) | URL to open | Optional|
|cache\_time|[int](/API_docs/types/int.html) | Cache validity | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->messages->setBotCallbackAnswer(alert: Bool, query_id: long, message: 'string', url: 'string', cache_time: int, );
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Bool](../types/Bool.html) will be returned instead.


