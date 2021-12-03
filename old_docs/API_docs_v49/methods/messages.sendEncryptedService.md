---
title: messages.sendEncryptedService
description: Sends a service message to a secret chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendEncryptedService.html
---
# Method: messages.sendEncryptedService
[Back to methods index](index.md)



Sends a service message to a secret chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | Secret chat ID | Yes|
|data|[bytes](../types/bytes.md) | TL-serialization of  [DecryptedMessage](../types/DecryptedMessage.md) type, encrypted with a key generated during chat initialization | Yes|


### Return type: [messages.SentEncryptedMessage](../types/messages.SentEncryptedMessage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncryptedService(['peer' => InputEncryptedChat, 'data' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
messages_SentEncryptedMessage = messages.sendEncryptedService({peer=InputEncryptedChat, data='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|DATA_INVALID|Encrypted data invalid|
|400|ENCRYPTION_DECLINED|The secret chat was declined|
|400|ENCRYPTION_ID_INVALID|The provided secret chat ID is invalid|
|400|MSG_WAIT_FAILED|A waiting call returned an error|
|400|USER_IS_BLOCKED|You were blocked by this user|
|403|USER_DELETED|You can't send this secret message because the other participant deleted their account.|
|403|USER_IS_BLOCKED|You were blocked by this user|


