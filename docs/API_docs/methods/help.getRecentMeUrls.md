---
title: "help.getRecentMeUrls"
description: "Get recently used `t.me` links"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getRecentMeUrls.html
---
# Method: help.getRecentMeUrls
[Back to methods index](index.md)



Get recently used `t.me` links

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|referer|[string](../types/string.md) | Referer | Yes|


### Return type: [help.RecentMeUrls](../types/help.RecentMeUrls.md)

### Can bots use this method: **NO**


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

