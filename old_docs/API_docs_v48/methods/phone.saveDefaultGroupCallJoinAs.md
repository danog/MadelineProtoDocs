---
title: phone.saveDefaultGroupCallJoinAs
description: phone.saveDefaultGroupCallJoinAs parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_saveDefaultGroupCallJoinAs.html
---
# Method: phone.saveDefaultGroupCallJoinAs
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|join\_as|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->phone->saveDefaultGroupCallJoinAs(['peer' => InputPeer, 'join_as' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
Bool = phone.saveDefaultGroupCallJoinAs({peer=InputPeer, join_as=InputPeer, })
```

