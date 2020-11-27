---
title: contacts.getTopPeers
description: Get most used peers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getTopPeers.html
---
# Method: contacts.getTopPeers
[Back to methods index](index.md)



Get most used peers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|correspondents|[Bool](../types/Bool.md) | Users we've chatted most frequently with | Optional|
|bots\_pm|[Bool](../types/Bool.md) | Most used bots | Optional|
|bots\_inline|[Bool](../types/Bool.md) | Most used inline bots | Optional|
|groups|[Bool](../types/Bool.md) | Often-opened groups and supergroups | Optional|
|channels|[Bool](../types/Bool.md) | Most frequently visited channels | Optional|
|offset|[int](../types/int.md) | Offset for [pagination](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [contacts.TopPeers](../types/contacts.TopPeers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_TopPeers = $MadelineProto->contacts->getTopPeers(['correspondents' => Bool, 'bots_pm' => Bool, 'bots_inline' => Bool, 'groups' => Bool, 'channels' => Bool, 'offset' => int, 'limit' => int, 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
contacts_TopPeers = contacts.getTopPeers({correspondents=Bool, bots_pm=Bool, bots_inline=Bool, groups=Bool, channels=Bool, offset=int, limit=int, hash={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|TYPES_EMPTY|No top peer type was provided|


