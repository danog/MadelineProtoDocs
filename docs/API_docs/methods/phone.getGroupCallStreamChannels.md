---
title: "phone.getGroupCallStreamChannels"
description: "Get info about RTMP streams in a group call or livestream.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_getGroupCallStreamChannels.html
---
# Method: phone.getGroupCallStreamChannels
[Back to methods index](index.html)



Get info about RTMP streams in a group call or livestream.  
This method should be invoked to the same group/channel-related DC used for [downloading livestream chunks](https://core.telegram.org/api/files#downloading-files).  
As usual, the media DC is preferred, if available.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Group call or livestream | Yes|


### Return type: [phone.GroupCallStreamChannels](/API_docs/types/phone.GroupCallStreamChannels.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$phone_GroupCallStreamChannels = $MadelineProto->phone->getGroupCallStreamChannels(call: $InputGroupCall, );
```

