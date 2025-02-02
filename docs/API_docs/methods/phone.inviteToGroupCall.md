---
title: "phone.inviteToGroupCall"
description: "Invite a set of users to a group call."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_inviteToGroupCall.html
---
# Method: phone.inviteToGroupCall
[Back to methods index](index.html)



Invite a set of users to a group call.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The group call | Yes|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The users to invite. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->phone->inviteToGroupCall(call: $InputGroupCall, users: [$InputUser, $InputUser], );
```

