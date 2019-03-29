---
title: help.getAppChangelog
description: Get the changelog of this app
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getAppChangelog  
[Back to methods index](index.md)


Get the changelog of this app

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|prev\_app\_version|[string](../types/string.md) | Previous app version | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->help->getAppChangelog(['prev_app_version' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = help.getAppChangelog({prev_app_version='string', })
```

