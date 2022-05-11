---
title: "messages.getSearchCounters"
description: "Get the number of results that would be found by a [messages.search](../methods/messages.search.html) call with the same parameters"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSearchCounters.html
---
# Method: messages.getSearchCounters
[Back to methods index](index.html)



Get the number of results that would be found by a [messages.search](../methods/messages.search.html) call with the same parameters

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where to search | Optional|
|filters|Array of [MessagesFilter](/API_docs/types/MessagesFilter.html) | Search filters | Yes|


### Return type: [Vector\_of\_messages.SearchCounter](/API_docs/types/messages.SearchCounter.html)

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
$Vector_of_messages_SearchCounter = $MadelineProto->messages->getSearchCounters(peer: InputPeer, filters: [MessagesFilter, MessagesFilter], );
```

