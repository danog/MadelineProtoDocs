---
title: "messages.setDefaultHistoryTTL"
description: "Changes the default value of the Time-To-Live setting, applied to all new chats."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setDefaultHistoryTTL.html
---
# Method: messages.setDefaultHistoryTTL
[Back to methods index](index.html)



Changes the default value of the Time-To-Live setting, applied to all new chats.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|period|[int](/API_docs/types/int.html) | The new default Time-To-Live of all messages sent in new chats, in seconds. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setDefaultHistoryTTL(period: $int, );
```

