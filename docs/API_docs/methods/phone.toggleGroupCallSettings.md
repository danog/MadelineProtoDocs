---
title: "phone.toggleGroupCallSettings"
description: "phone.toggleGroupCallSettings parameters, return type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_toggleGroupCallSettings.html
---
# Method: phone.toggleGroupCallSettings
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|reset\_invite\_hash|[Bool](../types/Bool.md) | Optional|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|join\_muted|[Bool](../types/Bool.md) | Optional|


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

$Updates = $MadelineProto->phone->toggleGroupCallSettings(['reset_invite_hash' => Bool, 'call' => InputGroupCall, 'join_muted' => Bool, ]);
```

Or, if you're into Lua:

```lua
Updates = phone.toggleGroupCallSettings({reset_invite_hash=Bool, call=InputGroupCall, join_muted=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|GROUPCALL_NOT_MODIFIED|Group call settings weren't modified|


