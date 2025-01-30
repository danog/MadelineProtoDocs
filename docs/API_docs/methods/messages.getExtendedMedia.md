---
title: "messages.getExtendedMedia"
description: "Fetch updated information about [paid media, see here »](https://core.telegram.org/api/paid-media) for the full flow."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getExtendedMedia.html
---
# Method: messages.getExtendedMedia
[Back to methods index](index.html)



Fetch updated information about [paid media, see here »](https://core.telegram.org/api/paid-media) for the full flow.

This method will return an array of [updateMessageExtendedMedia](../constructors/updateMessageExtendedMedia.html) updates, only for messages containing **already bought** paid media.  
No information will be returned for messages containing not yet bought paid media.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer with visible paid media messages. | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of currently visible messages containing paid media. | Yes|


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

$Updates = $MadelineProto->messages->getExtendedMedia(peer: $InputPeer, id: [$int, $int], );
```

