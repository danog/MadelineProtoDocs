---
title: phone.getGroupCallJoinAs
description: phone.getGroupCallJoinAs parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupCallJoinAs.html
---
# Method: phone.getGroupCallJoinAs
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|


### Return type: [phone.JoinAsPeers](../types/phone.JoinAsPeers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$phone_JoinAsPeers = $MadelineProto->phone->getGroupCallJoinAs(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
phone_JoinAsPeers = phone.getGroupCallJoinAs({peer=InputPeer, })
```

