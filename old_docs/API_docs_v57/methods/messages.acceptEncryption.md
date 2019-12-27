---
title: messages.acceptEncryption
description: Confirms creation of a secret chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.acceptEncryption  
[Back to methods index](index.md)


Confirms creation of a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | Secret chat ID | Yes|
|g\_b|[bytes](../types/bytes.md) | `B = g ^ b mod p`, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) | Yes|
|key\_fingerprint|[long](../types/long.md) | 64-bit fingerprint of the received key | Yes|


### Return type: [EncryptedChat](../types/EncryptedChat.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EncryptedChat = $MadelineProto->messages->acceptEncryption(['peer' => InputEncryptedChat, 'g_b' => 'bytes', 'key_fingerprint' => long, ]);
```

Or, if you're into Lua:

```lua
EncryptedChat = messages.acceptEncryption({peer=InputEncryptedChat, g_b='bytes', key_fingerprint=long, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|ENCRYPTION_ALREADY_ACCEPTED|Secret chat already accepted|
|400|ENCRYPTION_ALREADY_DECLINED|The secret chat was already declined|


