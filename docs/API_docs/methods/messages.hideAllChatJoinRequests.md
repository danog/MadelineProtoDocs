---
title: "messages.hideAllChatJoinRequests"
description: "Dismiss or approve all [join requests](https://core.telegram.org/api/invites#join-requests) related to a specific chat or channel."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_hideAllChatJoinRequests.html
---
# Method: messages.hideAllChatJoinRequests
[Back to methods index](index.html)



Dismiss or approve all [join requests](https://core.telegram.org/api/invites#join-requests) related to a specific chat or channel.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|approved|[Bool](/API_docs/types/Bool.html) | Whether to dismiss or approve all chat [join requests »](https://core.telegram.org/api/invites#join-requests) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat or channel | Optional|
|link|[string](/API_docs/types/string.html) | Only dismiss or approve [join requests »](https://core.telegram.org/api/invites#join-requests) initiated using this invite link | Optional|


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
$Updates = $MadelineProto->messages->hideAllChatJoinRequests(approved: Bool, peer: InputPeer, link: 'string', );
```

