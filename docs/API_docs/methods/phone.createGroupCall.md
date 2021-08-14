---
title: phone.createGroupCall
description: phone.createGroupCall parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_createGroupCall.html
---
# Method: phone.createGroupCall
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|title|[string](../types/string.md) | Optional|
|schedule\_date|[int](../types/int.md) | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->createGroupCall(['peer' => InputPeer, 'title' => 'string', 'schedule_date' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = phone.createGroupCall({peer=InputPeer, title='string', schedule_date=int, })
```

