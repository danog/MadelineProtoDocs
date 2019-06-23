---
title: help.getRecentMeUrls
description: Get recent t.me URLs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getRecentMeUrls  
[Back to methods index](index.md)


Get recent t.me URLs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|referer|[string](../types/string.md) | Referrer | Yes|


### Return type: [help\_RecentMeUrls](../types/help_RecentMeUrls.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_RecentMeUrls = $MadelineProto->help->getRecentMeUrls(['referer' => 'string', ]);
```

Or, if you're into Lua:

```lua
help_RecentMeUrls = help.getRecentMeUrls({referer='string', })
```

