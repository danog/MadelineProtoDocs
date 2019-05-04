---
title: phone.receivedCall
description: Notify server that you received a call (server will refuse all incoming calls until the current call is over)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: phone.receivedCall  
[Back to methods index](index.md)


Notify server that you received a call (server will refuse all incoming calls until the current call is over)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputPhoneCall](../types/InputPhoneCall.md) | The phone call you received | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->phone->receivedCall(['peer' => InputPhoneCall, ]);
```

Or, if you're into Lua:

```lua
Bool = phone.receivedCall({peer=InputPhoneCall, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CALL_ALREADY_DECLINED|The call was already declined|
|CALL_PEER_INVALID|The provided call peer object is invalid|

