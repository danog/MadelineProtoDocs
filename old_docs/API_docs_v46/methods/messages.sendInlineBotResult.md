---
title: messages.sendInlineBotResult
description: Send a result obtained using [messages.getInlineBotResults](../methods/messages.getInlineBotResults.md).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendInlineBotResult  
[Back to methods index](index.md)


Send a result obtained using [messages.getInlineBotResults](../methods/messages.getInlineBotResults.md).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Bool](../types/Bool.md) | Broadcast this message? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Destination | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | ID of the message this message should reply to | Optional|
|query\_id|[long](../types/long.md) | Query ID from [messages.getInlineBotResults](../methods/messages.getInlineBotResults.md) | Yes|
|id|[string](../types/string.md) | Result ID from [messages.getInlineBotResults](../methods/messages.getInlineBotResults.md) | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendInlineBotResult(['broadcast' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'query_id' => long, 'id' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendInlineBotResult({broadcast=Bool, peer=InputPeer, reply_to_msg_id=int, query_id=long, id='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INLINE_RESULT_EXPIRED|The inline query expired|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|QUERY_ID_EMPTY|The query ID is empty|
|400|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|
|400|WEBPAGE_MEDIA_EMPTY|Webpage media empty|
|400|YOU_BLOCKED_USER|You blocked this user|
|403|CHAT_SEND_INLINE_FORBIDDEN|You can't send inline messages in this group|
|403|CHAT_SEND_MEDIA_FORBIDDEN|You can't send media in this chat|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


