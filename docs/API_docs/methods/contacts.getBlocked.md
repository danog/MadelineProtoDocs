---
title: "contacts.getBlocked"
description: "Returns the list of blocked users."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getBlocked.html
---
# Method: contacts.getBlocked
[Back to methods index](index.md)



Returns the list of blocked users.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | The number of list elements to be skipped | Yes|
|limit|[int](../types/int.md) | The number of list elements to be returned | Yes|


### Return type: [contacts.Blocked](../types/contacts.Blocked.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_Blocked = $MadelineProto->contacts->getBlocked(['offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
contacts_Blocked = contacts.getBlocked({offset=int, limit=int, })
```

