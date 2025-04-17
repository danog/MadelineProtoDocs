---
title: "messages.clickSponsoredMessage"
description: "Informs the server that the user has interacted with a sponsored message in [one of the ways listed here »](https://core.telegram.org/api/sponsored-messages#clicking-on-sponsored-messages)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_clickSponsoredMessage.html
---
# Method: messages.clickSponsoredMessage
[Back to methods index](index.html)



Informs the server that the user has interacted with a sponsored message in [one of the ways listed here »](https://core.telegram.org/api/sponsored-messages#clicking-on-sponsored-messages).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|media|[Bool](/API_docs/types/Bool.html) | The user clicked on the media | Optional|
|fullscreen|[Bool](/API_docs/types/Bool.html) | The user expanded the video to full screen, and then clicked on it. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The channel/bot where the ad is located | Optional|
|random\_id|[bytes](/API_docs/types/bytes.html) | The ad's unique ID. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->messages->clickSponsoredMessage(media: $Bool, fullscreen: $Bool, peer: $InputPeer, random_id: 'bytes', );
```

