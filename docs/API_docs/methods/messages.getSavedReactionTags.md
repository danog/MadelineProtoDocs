---
title: "messages.getSavedReactionTags"
description: "Fetch the full list of [saved message tags](https://core.telegram.org/api/saved-messages#tags) created by the user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSavedReactionTags.html
---
# Method: messages.getSavedReactionTags
[Back to methods index](index.html)



Fetch the full list of [saved message tags](https://core.telegram.org/api/saved-messages#tags) created by the user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, returns tags only used in the specified [saved message dialog](https://core.telegram.org/api/saved-messages#saved-message-dialogs). | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). | Optional|


### Return type: [messages.SavedReactionTags](/API_docs/types/messages.SavedReactionTags.html)

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

$messages_SavedReactionTags = $MadelineProto->messages->getSavedReactionTags(peer: $InputPeer, hash: [$long\|string, $long\|string], );
```

