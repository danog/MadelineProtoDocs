---
title: "messages.getSearchResultsCalendar"
description: "messages.getSearchResultsCalendar parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSearchResultsCalendar.html
---
# Method: messages.getSearchResultsCalendar
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.html) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Yes|
|offset\_date|[int](/API_docs/types/int.html) | Yes|


### Return type: [messages.SearchResultsCalendar](/API_docs/types/messages.SearchResultsCalendar.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SearchResultsCalendar = $MadelineProto->messages->getSearchResultsCalendar(['peer' => InputPeer, 'filter' => MessagesFilter, 'offset_id' => int, 'offset_date' => int, ]);
```

