---
title: "messages.search"
description: "Search for messages."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_search.html
---
# Method: messages.search
[Back to methods index](index.html)



Search for messages.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | User or chat, histories with which are searched, or [(inputPeerEmpty)](../constructors/inputPeerEmpty.html) constructor to search in all private chats and [normal groups (not channels) »](https://core.telegram.org/api/channel). Use [messages.searchGlobal](../methods/messages.searchGlobal.html) to search globally in all chats, groups, supergroups and channels. | Optional|
|q|[string](/API_docs/types/string.html) | Text search request | Optional|
|from\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Only return messages sent by the specified user ID | Optional|
|saved\_peer\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Search within the [saved message dialog »](https://core.telegram.org/api/saved-messages) with this ID. | Optional|
|saved\_reaction|Array of [Reaction](/API_docs/types/Reaction.html) | You may search for [saved messages tagged »](https://core.telegram.org/api/saved-messages#tags) with one or more reactions using this flag. | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | [Thread ID](https://core.telegram.org/api/threads) | Optional|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.html) | Filter to return only specified message types | Optional|
|min\_date|[int](/API_docs/types/int.html) | If a positive value was transferred, only messages with a sending date bigger than the transferred one will be returned | Optional|
|max\_date|[int](/API_docs/types/int.html) | If a positive value was transferred, only messages with a sending date smaller than the transferred one will be returned | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Only return messages starting from the specified message ID | Optional|
|add\_offset|[int](/API_docs/types/int.html) | [Additional offset](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | [Number of results to return](https://core.telegram.org/api/offsets), can be 0 to only return the message counter. | Optional|
|max\_id|[int](/API_docs/types/int.html) | [Maximum message ID to return](https://core.telegram.org/api/offsets) | Optional|
|min\_id|[int](/API_docs/types/int.html) | [Minimum message ID to return](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash](https://core.telegram.org/api/offsets) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->search(peer: $InputPeer, q: 'string', from_id: $InputPeer, saved_peer_id: $InputPeer, saved_reaction: [$Reaction, $Reaction], top_msg_id: $int, filter: $MessagesFilter, min_date: $int, max_date: $int, offset_id: $int, add_offset: $int, limit: $int, max_id: $int, min_id: $int, hash: [$long\|string, $long\|string], );
```

