---
title: messages.sendEncryptedService
description: Send a service message to a secret chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendEncryptedService  
[Back to methods index](index.md)


Send a service message to a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | The chat where to send the service message | Yes|
|message|[DecryptedMessage](../types/DecryptedMessage.md) | The service message | Yes|


### Return type: [messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncryptedService(['peer' => InputEncryptedChat, 'message' => DecryptedMessage, ]);
```

Or, if you're into Lua:

```lua
messages_SentEncryptedMessage = messages.sendEncryptedService({peer=InputEncryptedChat, message=DecryptedMessage, })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md) will be returned instead.


### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|DATA_INVALID|Encrypted data invalid|
|ENCRYPTION_DECLINED|The secret chat was declined|
|MSG_WAIT_FAILED|A waiting call returned an error|
|USER_IS_BLOCKED|User is blocked|


