---
title: "phone.exportGroupCallInvite"
description: "Get an [invite link](https://core.telegram.org/api/links#voice-chatvideo-chatlivestream-links) for a group call or livestream"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_exportGroupCallInvite.html
---
# Method: phone.exportGroupCallInvite
[Back to methods index](index.html)



Get an [invite link](https://core.telegram.org/api/links#voice-chatvideo-chatlivestream-links) for a group call or livestream

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|can\_self\_unmute|[Bool](/API_docs/types/Bool.html) | For livestreams or muted group chats, if set, users that join using this link will be able to speak without explicitly requesting permission by (for example by raising their hand). | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The group call | Yes|


### Return type: [phone.ExportedGroupCallInvite](/API_docs/types/phone.ExportedGroupCallInvite.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$phone_ExportedGroupCallInvite = $MadelineProto->phone->exportGroupCallInvite(can_self_unmute: Bool, call: InputGroupCall, );
```

