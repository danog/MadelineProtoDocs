---
title: "phone.joinGroupCall"
description: "Join a group call"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_joinGroupCall.html
---
# Method: phone.joinGroupCall
[Back to methods index](index.html)



Join a group call

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|muted|[Bool](/API_docs/types/Bool.html) | If set, the user will be muted by default upon joining. | Optional|
|video\_stopped|[Bool](/API_docs/types/Bool.html) | If set, the user's video will be disabled by default upon joining. | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The group call | Yes|
|join\_as|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Join the group call, presenting yourself as the specified user/channel | Optional|
|invite\_hash|[string](/API_docs/types/string.html) | The invitation hash from the invite link: `https://t.me/username?voicechat=hash` | Optional|
|params|[DataJSON](/API_docs/types/DataJSON.html) | WebRTC parameters | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->phone->joinGroupCall(muted: Bool, video_stopped: Bool, call: InputGroupCall, join_as: InputPeer, invite_hash: 'string', params: DataJSON, );
```

