---
title: messages.readEncryptedHistory
description: Mark messages as read in secret chats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.readEncryptedHistory  
[Back to methods index](index.md)


Mark messages as read in secret chats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | The secret chat where to mark messages as read | Yes|
|max\_date|[int](../types/int.md) | Maximum date of messages to mark | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->readEncryptedHistory(['peer' => InputEncryptedChat, 'max_date' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.readEncryptedHistory({peer=InputEncryptedChat, max_date=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|MSG_WAIT_FAILED|A waiting call returned an error|


