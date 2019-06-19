---
title: get_future_salts
description: Get future salts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: get\_future\_salts  
[Back to methods index](index.md)


Get future salts

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|num|[int](../types/int.md) | How many salts should be fetched | Yes|


### Return type: [FutureSalts](../types/FutureSalts.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$FutureSalts = $MadelineProto->get_future_salts(['num' => int, ]);
```

Or, if you're into Lua:

```lua
FutureSalts = get_future_salts({num=int, })
```

