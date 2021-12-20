---
title: "phone.joinGroupCall"
description: "phone.joinGroupCall parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_joinGroupCall.html
---
# Method: phone.joinGroupCall
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|muted|[Bool](../types/Bool.md) | Optional|
|video\_stopped|[Bool](../types/Bool.md) | Optional|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|join\_as|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|invite\_hash|[string](../types/string.md) | Optional|
|params|[DataJSON](../types/DataJSON.md) | Yes|


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

$Updates = $MadelineProto->phone->joinGroupCall(['muted' => Bool, 'video_stopped' => Bool, 'call' => InputGroupCall, 'join_as' => InputPeer, 'invite_hash' => 'string', 'params' => DataJSON, ]);
```

Or, if you're into Lua:

```lua
Updates = phone.joinGroupCall({muted=Bool, video_stopped=Bool, call=InputGroupCall, join_as=InputPeer, invite_hash='string', params=DataJSON, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|GROUPCALL_SSRC_DUPLICATE_MUCH|The app needs to retry joining the group call with a new SSRC value.|


