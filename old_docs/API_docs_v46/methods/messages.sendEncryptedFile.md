---
title: messages.sendEncryptedFile
description: Sends a message with a file attachment to a secret chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendEncryptedFile  
[Back to methods index](index.md)


Sends a message with a file attachment to a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | Secret chat ID | Yes|
|message|[DecryptedMessage](../types/DecryptedMessage.md) | The message with the file | Yes|
|file|[File path or InputEncryptedFile](../types/InputEncryptedFile.md) | File attachment for the secret chat | Optional|


### Return type: [messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncryptedFile(['peer' => InputEncryptedChat, 'message' => DecryptedMessage, 'file' => InputEncryptedFile, ]);
```

Or, if you're into Lua:

```lua
messages_SentEncryptedMessage = messages.sendEncryptedFile({peer=InputEncryptedChat, message=DecryptedMessage, file=InputEncryptedFile, })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md) will be returned instead.


### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|DATA_TOO_LONG|Data too long|
|400|MD5_CHECKSUM_INVALID|The MD5 checksums do not match|
|400|MSG_WAIT_FAILED|A waiting call returned an error|


