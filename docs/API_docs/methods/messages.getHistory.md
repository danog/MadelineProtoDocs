---
title: "messages.getHistory"
description: "Returns the conversation history with one interlocutor / within a chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getHistory.html
---
# Method: messages.getHistory
[Back to methods index](index.html)



# Warning: flood wait
**Warning: this method is prone to rate limiting with flood waits, **which can lead to !!! ACCOUNT BANS !!!**, please use the [updates event handler, instead (which is 100% safe) &raquo;](/docs/UPDATES.html#async-event-driven)**

# Warning: non-realtime results
**Warning: this method is not suitable for receiving messages in real-time from chats and users, please use the [updates event handler, instead &raquo;](/docs/UPDATES.html#async-event-driven)**

# Warning: this is probably NOT what you need
You probably need to use the [updates event handler, instead &raquo;](/docs/UPDATES.html#async-event-driven) :)

Returns the conversation history with one interlocutor / within a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Target peer | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Only return messages starting from the specified message ID | Optional|
|offset\_date|[int](/API_docs/types/int.html) | Only return messages sent before the specified date | Optional|
|add\_offset|[int](/API_docs/types/int.html) | Number of list elements to be skipped, negative values are also accepted. | Optional|
|limit|[int](/API_docs/types/int.html) | Number of results to return | Optional|
|max\_id|[int](/API_docs/types/int.html) | If a positive value was transferred, the method will return only messages with IDs less than **max\_id** | Optional|
|min\_id|[int](/API_docs/types/int.html) | If a positive value was transferred, the method will return only messages with IDs more than **min\_id** | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Result hash](https://core.telegram.org/api/offsets) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getHistory(peer: $InputPeer, offset_id: $int, offset_date: $int, add_offset: $int, limit: $int, max_id: $int, min_id: $int, hash: [$long\|string, $long\|string], );
```

