---
title: messages.sendEncryptedFile
description: Sends a message with a file attachment to a secret chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendEncryptedFile.html
---
# Method: messages.sendEncryptedFile
[Back to methods index](index.md)



Sends a message with a file attachment to a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) |  | Optional|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | Secret chat ID | Yes|
|data|[bytes](../types/bytes.md) | [DecryptedMessage](../types/DecryptedMessage.md) type | Yes|
|file|[File path or InputEncryptedFile](../types/InputEncryptedFile.md) | File attachment for the secret chat | Optional|


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

$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncryptedFile(['silent' => Bool, 'peer' => InputEncryptedChat, 'data' => 'bytes', 'file' => InputEncryptedFile, ]);
```

Or, if you're into Lua:

```lua
messages_SentEncryptedMessage = messages.sendEncryptedFile({silent=Bool, peer=InputEncryptedChat, data='bytes', file=InputEncryptedFile, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|DATA_TOO_LONG|Data too long|
|400|ENCRYPTION_DECLINED|The secret chat was declined|
|400|MD5_CHECKSUM_INVALID|The MD5 checksums do not match|
|400|MSG_WAIT_FAILED|A waiting call returned an error|


