---
title: messages.sendInlineBotResult
description: Send inline bot result obtained with messages.getInlineBotResults to the chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendInlineBotResult  
[Back to methods index](index.md)


Send inline bot result obtained with messages.getInlineBotResults to the chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Disable notifications? | Optional|
|background|[Bool](../types/Bool.md) | Disable background notifications? | Optional|
|clear\_draft|[Bool](../types/Bool.md) | Clear the message draft? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to send the message | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | Reply to message by ID | Optional|
|query\_id|[long](../types/long.md) | The inline query ID | Yes|
|id|[string](../types/string.md) | The ID of one of the inline results | Yes|


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

$Updates = $MadelineProto->messages->sendInlineBotResult(['silent' => Bool, 'background' => Bool, 'clear_draft' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'query_id' => long, 'id' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendInlineBotResult({silent=Bool, background=Bool, clear_draft=Bool, peer=InputPeer, reply_to_msg_id=int, query_id=long, id='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|INLINE_RESULT_EXPIRED|The inline query expired|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|QUERY_ID_EMPTY|The query ID is empty|
|400|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|
|400|WEBPAGE_MEDIA_EMPTY|Webpage media empty|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


