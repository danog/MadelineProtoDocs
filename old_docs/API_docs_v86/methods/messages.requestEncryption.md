---
title: messages.requestEncryption
description: You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_requestEncryption.html
---
# Method: messages.requestEncryption  
[Back to methods index](index.md)


You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats | Optional|
|g\_a|[bytes](../types/bytes.md) | You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling secret chats | Yes|


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


