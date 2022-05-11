---
title: "phone.createGroupCall"
description: "Create a group call or livestream"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_createGroupCall.html
---
# Method: phone.createGroupCall
[Back to methods index](index.html)



Create a group call or livestream

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|rtmp\_stream|[Bool](/API_docs/types/Bool.html) | Whether RTMP stream support should be enabled: only the [group/supergroup/channel](https://core.telegram.org/api/channel) owner can use this flag. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Associate the group call or livestream to the provided [group/supergroup/channel](https://core.telegram.org/api/channel) | Optional|
|title|[string](/API_docs/types/string.html) | Call title | Optional|
|schedule\_date|[int](/API_docs/types/int.html) | For scheduled group call or livestreams, the absolute date when the group call will start | Optional|


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
$Updates = $MadelineProto->phone->createGroupCall(rtmp_stream: Bool, peer: InputPeer, title: 'string', schedule_date: int, );
```

