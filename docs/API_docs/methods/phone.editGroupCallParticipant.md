---
title: "phone.editGroupCallParticipant"
description: "Edit information about a given group call participant"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_editGroupCallParticipant.html
---
# Method: phone.editGroupCallParticipant
[Back to methods index](index.html)



Edit information about a given group call participant

Note: [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).N?[Bool](../types/Bool.html) parameters can have three possible values:

- If the [TL flag](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) is not set, the previous value will not be changed.
- If the [TL flag](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) is set and contains a [boolTrue](../constructors/boolTrue.html), the previous value will be overwritten to `true`.
- If the [TL flag](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) is set and contains a [boolFalse](../constructors/boolFalse.html), the previous value will be overwritten to `false`.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | The group call | Yes|
|participant|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The group call participant (can also be the user itself) | Optional|
|muted|[Bool](/API_docs/types/Bool.html) | Whether to mute or unmute the specified participant | Optional|
|volume|[int](/API_docs/types/int.html) | New volume | Optional|
|raise\_hand|[Bool](/API_docs/types/Bool.html) | Raise or lower hand | Optional|
|video\_stopped|[Bool](/API_docs/types/Bool.html) | Start or stop the video stream | Optional|
|video\_paused|[Bool](/API_docs/types/Bool.html) | Pause or resume the video stream | Optional|
|presentation\_paused|[Bool](/API_docs/types/Bool.html) | Pause or resume the screen sharing stream | Optional|


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
$Updates = $MadelineProto->phone->editGroupCallParticipant(call: InputGroupCall, participant: InputPeer, muted: Bool, volume: int, raise_hand: Bool, video_stopped: Bool, video_paused: Bool, presentation_paused: Bool, );
```

