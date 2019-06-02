---
title: geochats.search
description: Search messages in geocha
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: geochats.search  
[Back to methods index](index.md)


Search messages in geocha

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | The geochat | Yes|
|q|[string](../types/string.md) | The search query | Yes|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Search filter | Optional|
|min\_date|[int](../types/int.md) | Minumum date | Yes|
|max\_date|[int](../types/int.md) | Maximum date | Yes|
|offset|[int](../types/int.md) | Offset | Yes|
|max\_id|[int](../types/int.md) | Maximum message ID | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [geochats\_Messages](../types/geochats_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats_Messages = $MadelineProto->geochats->search(['peer' => InputGeoChat, 'q' => 'string', 'filter' => MessagesFilter, 'min_date' => int, 'max_date' => int, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
geochats_Messages = geochats.search({peer=InputGeoChat, q='string', filter=MessagesFilter, min_date=int, max_date=int, offset=int, max_id=int, limit=int, })
```

