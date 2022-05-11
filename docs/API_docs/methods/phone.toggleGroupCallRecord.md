---
title: "phone.toggleGroupCallRecord"
description: "Start or stop recording a group call: the recorded audio and video streams will be automatically sent to `Saved messages` (the chat with ourselves)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_toggleGroupCallRecord.html
---
# Method: phone.toggleGroupCallRecord
[Back to methods index](index.html)



Start or stop recording a group call: the recorded audio and video streams will be automatically sent to `Saved messages` (the chat with ourselves).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|start|[Bool](/API_docs/types/Bool.html) | Whether to start or stop recording | Optional|
|video|[Bool](/API_docs/types/Bool.html) | Whether to also record video streams | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The group call or livestream | Yes|
|title|[string](/API_docs/types/string.html) | Recording title | Optional|
|video\_portrait|[Bool](/API_docs/types/Bool.html) | If video stream recording is enabled, whether to record in portrait or landscape mode | Optional|


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
$Updates = $MadelineProto->phone->toggleGroupCallRecord(start: Bool, video: Bool, call: InputGroupCall, title: 'string', video_portrait: Bool, );
```

