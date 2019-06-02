---
title: account.updateDeviceLocked
description: Disable all notifications for a certain period
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.updateDeviceLocked  
[Back to methods index](index.md)


Disable all notifications for a certain period

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|period|[int](../types/int.md) | For how long should notifications be disabled | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->updateDeviceLocked(['period' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = account.updateDeviceLocked({period=int, })
```

