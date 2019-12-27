---
title: account.getNotifyExceptions
description: Returns list of chats with non-default notification settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getNotifyExceptions.html
---
# Method: account.getNotifyExceptions  
[Back to methods index](index.md)


Returns list of chats with non-default notification settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|compare\_sound|[Bool](../types/Bool.md) | If true, chats with non-default sound will also be returned | Optional|
|peer|[Username, chat ID, Update, Message or InputNotifyPeer](../types/InputNotifyPeer.md) | If specified, only chats of the specified category will be returned | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->account->getNotifyExceptions(['compare_sound' => Bool, 'peer' => InputNotifyPeer, ]);
```

Or, if you're into Lua:

```lua
Updates = account.getNotifyExceptions({compare_sound=Bool, peer=InputNotifyPeer, })
```

