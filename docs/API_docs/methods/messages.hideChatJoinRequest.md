---
title: "messages.hideChatJoinRequest"
description: "Dismiss or approve a chat [join request](https://core.telegram.org/api/invites#join-requests) related to a specific chat or channel."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_hideChatJoinRequest.html
---
# Method: messages.hideChatJoinRequest
[Back to methods index](index.html)



Dismiss or approve a chat [join request](https://core.telegram.org/api/invites#join-requests) related to a specific chat or channel.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|approved|[Bool](/API_docs/types/Bool.html) | Whether to dismiss or approve the chat [join request »](https://core.telegram.org/api/invites#join-requests) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat or channel | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user whose [join request »](https://core.telegram.org/api/invites#join-requests) should be dismissed or approved | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->messages->hideChatJoinRequest(approved: Bool, peer: InputPeer, user_id: InputUser, );
```

