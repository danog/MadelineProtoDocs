---
title: "messages.getSearchResultsPositions"
description: "Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSearchResultsPositions.html
---
# Method: messages.getSearchResultsPositions
[Back to methods index](index.html)



Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation.

Returns the results in reverse chronological order (i.e., in order of decreasing message\_id).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where to search | Optional|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.html) | Message filter, [inputMessagesFilterEmpty](../constructors/inputMessagesFilterEmpty.html), [inputMessagesFilterMyMentions](../constructors/inputMessagesFilterMyMentions.html) filters are not supported by this method. | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.SearchResultsPositions](/API_docs/types/messages.SearchResultsPositions.html)

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
$messages_SearchResultsPositions = $MadelineProto->messages->getSearchResultsPositions(peer: InputPeer, filter: MessagesFilter, offset_id: int, limit: int, );
```

