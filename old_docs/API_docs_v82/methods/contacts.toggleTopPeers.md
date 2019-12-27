---
title: contacts.toggleTopPeers
description: Enable/disable [top peers](https://core.telegram.org/api/top-rating)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.toggleTopPeers  
[Back to methods index](index.md)


Enable/disable [top peers](https://core.telegram.org/api/top-rating)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|enabled|[Bool](../types/Bool.md) | Enable/disable | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->contacts->toggleTopPeers(['enabled' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = contacts.toggleTopPeers({enabled=Bool, })
```

