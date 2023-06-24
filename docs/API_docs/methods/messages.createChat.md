---
title: "messages.createChat"
description: "Creates a new chat."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_createChat.html
---
# Method: messages.createChat
[Back to methods index](index.html)



Creates a new chat.

May also return 0-N updates of type [updateGroupInvitePrivacyForbidden](../constructors/updateGroupInvitePrivacyForbidden.html): it indicates we couldn't add a user to a chat because of their privacy settings; if required, an [invite link](https://core.telegram.org/api/invites) can be shared with the user, instead.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | List of user IDs to be invited | Yes|
|title|[string](/API_docs/types/string.html) | Chat name | Yes|
|ttl\_period|[int](/API_docs/types/int.html) | Time-to-live of all messages that will be sent in the chat: once message.date+message.ttl\_period === time(), the message will be deleted on the server, and must be deleted locally as well. You can use [messages.setDefaultHistoryTTL](../methods/messages.setDefaultHistoryTTL.html) to edit this value later. | Optional|


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

$Updates = $MadelineProto->messages->createChat(users: [$InputUser, $InputUser], title: 'string', ttl_period: $int, );
```

