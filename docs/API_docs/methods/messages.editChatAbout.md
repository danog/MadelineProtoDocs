---
title: "messages.editChatAbout"
description: "Edit the description of a [group/supergroup/channel](https://core.telegram.org/api/channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editChatAbout.html
---
# Method: messages.editChatAbout
[Back to methods index](index.html)



Edit the description of a [group/supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The [group/supergroup/channel](https://core.telegram.org/api/channel). | Optional|
|about|[string](/API_docs/types/string.html) | The new description | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->editChatAbout(['peer' => InputPeer, 'about' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ABOUT_NOT_MODIFIED|About text has not changed|
|400|CHAT_ABOUT_TOO_LONG|Chat about too long|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


