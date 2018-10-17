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
|broadcast|[Bool](../types/Bool.md) | Broadcast this message? | Optional|
|silent|[Bool](../types/Bool.md) | Disable notifications? | Optional|
|background|[Bool](../types/Bool.md) | Disable background notifications? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to send the message | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | Reply to message by ID | Optional|
|query\_id|[long](../types/long.md) | The inline query ID | Yes|
|id|[string](../types/string.md) | The ID of one of the inline results | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendInlineBotResult(['broadcast' => Bool, 'silent' => Bool, 'background' => Bool, 'peer' => InputPeer, 'reply_to_msg_id' => int, 'query_id' => long, 'id' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.sendInlineBotResult`

Parameters:

broadcast - Json encoded Bool

silent - Json encoded Bool

background - Json encoded Bool

peer - Json encoded InputPeer

reply_to_msg_id - Json encoded int

query_id - Json encoded long

id - Json encoded string




Or, if you're into Lua:

```lua
Updates = messages.sendInlineBotResult({broadcast=Bool, silent=Bool, background=Bool, peer=InputPeer, reply_to_msg_id=int, query_id=long, id='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|INLINE_RESULT_EXPIRED|The inline query expired|
|PEER_ID_INVALID|The provided peer id is invalid|
|QUERY_ID_EMPTY|The query ID is empty|
|WEBPAGE_CURL_FAILED|Failure while fetching the webpage with cURL|
|WEBPAGE_MEDIA_EMPTY|Webpage media empty|
|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


