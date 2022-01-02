---
title: "messages.getSearchResultsPositions"
description: "messages.getSearchResultsPositions parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSearchResultsPositions.html
---
# Method: messages.getSearchResultsPositions
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Optional|
|offset\_id|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|


### Return type: [messages.SearchResultsPositions](../types/messages.SearchResultsPositions.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SearchResultsPositions = $MadelineProto->messages->getSearchResultsPositions(['peer' => InputPeer, 'filter' => MessagesFilter, 'offset_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_SearchResultsPositions = messages.getSearchResultsPositions({peer=InputPeer, filter=MessagesFilter, offset_id=int, limit=int, })
```

