---
title: "channels.clickSponsoredMessage"
description: "Informs the server that the user has either"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_clickSponsoredMessage.html
---
# Method: channels.clickSponsoredMessage
[Back to methods index](index.html)



Informs the server that the user has either:

- Clicked on a link in the sponsored message
- Has opened a sponsored chat or a sponsored website via the associated button
- Has opened the sponsored chat via the sponsored message name, the sponsored message photo, or a mention in the sponsored message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|media|[Bool](/API_docs/types/Bool.html) |  | Optional|
|fullscreen|[Bool](/API_docs/types/Bool.html) |  | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel where the sponsored message was posted | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->clickSponsoredMessage(media: $Bool, fullscreen: $Bool, channel: $InputChannel, );
```

