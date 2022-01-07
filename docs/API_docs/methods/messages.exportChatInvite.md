---
title: "messages.exportChatInvite"
description: "Export an invite link for a chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_exportChatInvite.html
---
# Method: messages.exportChatInvite
[Back to methods index](index.md)



Export an invite link for a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|legacy\_revoke\_permanent|[Bool](/API_docs/types/Bool.md) |  | Optional|
|request\_needed|[Bool](/API_docs/types/Bool.md) |  | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | Chat | Optional|
|expire\_date|[int](/API_docs/types/int.md) |  | Optional|
|usage\_limit|[int](/API_docs/types/int.md) |  | Optional|
|title|[string](/API_docs/types/string.md) |  | Optional|


### Return type: [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedChatInvite = $MadelineProto->messages->exportChatInvite(['legacy_revoke_permanent' => Bool, 'request_needed' => Bool, 'peer' => InputPeer, 'expire_date' => int, 'usage_limit' => int, 'title' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|EXPIRE_DATE_INVALID|The specified expiration date is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|USAGE_LIMIT_INVALID|The specified usage limit is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


