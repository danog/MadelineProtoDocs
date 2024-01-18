---
title: "messages.getSavedDialogs"
description: "messages.getSavedDialogs parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSavedDialogs.html
---
# Method: messages.getSavedDialogs
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|exclude\_pinned|[Bool](/API_docs/types/Bool.html) | Optional|
|offset\_date|[int](/API_docs/types/int.html) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Optional|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|
|hash|Array of [long](/API_docs/types/long.html) | Optional|


### Return type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SavedDialogs = $MadelineProto->messages->getSavedDialogs(exclude_pinned: $Bool, offset_date: $int, offset_id: $int, offset_peer: $InputPeer, limit: $int, hash: [$long, $long], );
```

