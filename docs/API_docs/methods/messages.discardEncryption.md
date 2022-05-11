---
title: "messages.discardEncryption"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_discardEncryption.html
---
# Method: messages.discardEncryption
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|delete\_history|[Bool](/API_docs/types/Bool.html) | Whether to delete the entire chat history for the other user as well | Optional|
|chat\_id|[int](/API_docs/types/int.html) | Secret chat ID | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->discardEncryption(delete_history: Bool, chat_id: int, );
```

