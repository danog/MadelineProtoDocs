---
title: "messages.requestEncryption"
description: "Sends a request to start a secret chat to the user."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestEncryption.html
---
# Method: messages.requestEncryption
[Back to methods index](index.md)



Sends a request to start a secret chat to the user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|
|g\_a|[bytes](../types/bytes.md) | `A = g ^ a mod p`, see [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) | Yes|


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

$EncryptedChat = $MadelineProto->messages->requestEncryption(['user_id' => InputUser, 'g_a' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
EncryptedChat = messages.requestEncryption({user_id=InputUser, g_a='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|DH_G_A_INVALID|g_a invalid|
|400|USER_ID_INVALID|The provided user ID is invalid|


