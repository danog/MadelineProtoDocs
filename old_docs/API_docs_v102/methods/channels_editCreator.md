---
title: channels.editCreator
description: Edit creator of channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.editCreator  
[Back to methods index](index.md)


Edit creator of channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | Password | Yes|


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

$Updates = $MadelineProto->channels->editCreator(['channel' => InputChannel, 'user_id' => InputUser, 'password' => InputCheckPasswordSRP, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.editCreator({channel=InputChannel, user_id=InputUser, password=InputCheckPasswordSRP, })
```

