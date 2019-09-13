---
title: phone.setCallRating
description: Set phone call rating
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: phone.setCallRating  
[Back to methods index](index.md)


Set phone call rating

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_initiative|[Bool](../types/Bool.md) | User initiative | Optional|
|peer|[InputPhoneCall](../types/InputPhoneCall.md) | The phone call | Yes|
|rating|[int](../types/int.md) | Rating (1-5 stars) | Yes|
|comment|[string](../types/string.md) | An optional comment | Yes|


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

$Updates = $MadelineProto->phone->setCallRating(['user_initiative' => Bool, 'peer' => InputPhoneCall, 'rating' => int, 'comment' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = phone.setCallRating({user_initiative=Bool, peer=InputPhoneCall, rating=int, comment='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CALL_PEER_INVALID|The provided call peer object is invalid|


