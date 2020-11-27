---
title: messages.searchGifs
description: Search for GIFs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchGifs.html
---
# Method: messages.searchGifs
[Back to methods index](index.md)



Search for GIFs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|q|[string](../types/string.md) | Text query | Yes|
|offset|[int](../types/int.md) | Offset for [pagination »](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.FoundGifs](../types/messages.FoundGifs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FoundGifs = $MadelineProto->messages->searchGifs(['q' => 'string', 'offset' => int, ]);
```

Or, if you're into Lua:

```lua
messages_FoundGifs = messages.searchGifs({q='string', offset=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|SEARCH_QUERY_EMPTY|The search query is empty|


