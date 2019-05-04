---
title: help.getNearestDc
description: Get nearest datacenter
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getNearestDc  
[Back to methods index](index.md)


Get nearest datacenter



### Return type: [NearestDc](../types/NearestDc.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$NearestDc = $MadelineProto->help->getNearestDc();
```

Or, if you're into Lua:

```lua
NearestDc = help.getNearestDc({})
```

