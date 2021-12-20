---
title: "messages.readEncryptedHistory"
description: "Marks message history within a secret chat as read."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readEncryptedHistory.html
---
# Method: messages.readEncryptedHistory
[Back to methods index](index.md)



Marks message history within a secret chat as read.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | Secret chat ID | Yes|
|max\_date|[int](../types/int.md) | Maximum date value for received messages in history | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->readEncryptedHistory(['peer' => InputEncryptedChat, 'max_date' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.readEncryptedHistory({peer=InputEncryptedChat, max_date=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MSG_WAIT_FAILED|A waiting call returned an error|


