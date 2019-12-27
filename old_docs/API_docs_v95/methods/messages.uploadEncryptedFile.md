---
title: messages.uploadEncryptedFile
description: Upload encrypted file and associate it to a secret chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.uploadEncryptedFile  
[Back to methods index](index.md)


Upload encrypted file and associate it to a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | The secret chat to associate the file to | Yes|
|file|[File path or InputEncryptedFile](../types/InputEncryptedFile.md) | The file | Optional|


### Return type: [EncryptedFile](../types/EncryptedFile.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EncryptedFile = $MadelineProto->messages->uploadEncryptedFile(['peer' => InputEncryptedChat, 'file' => InputEncryptedFile, ]);
```

Or, if you're into Lua:

```lua
EncryptedFile = messages.uploadEncryptedFile({peer=InputEncryptedChat, file=InputEncryptedFile, })
```

