---
title: "messages.deletePhoneCallHistory"
description: "Delete the entire phone call history."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deletePhoneCallHistory.html
---
# Method: messages.deletePhoneCallHistory
[Back to methods index](index.html)



Delete the entire phone call history.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoke|[Bool](/API_docs/types/Bool.html) | Whether to remove phone call history for participants as well | Optional|


### Return type: [messages.AffectedFoundMessages](/API_docs/types/messages.AffectedFoundMessages.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_AffectedFoundMessages = $MadelineProto->messages->deletePhoneCallHistory(revoke: Bool, );
```

