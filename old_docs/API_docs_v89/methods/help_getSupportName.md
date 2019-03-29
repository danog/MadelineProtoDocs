---
title: help.getSupportName
description: Get support name
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getSupportName  
[Back to methods index](index.md)


Get support name



### Return type: [help\_SupportName](../types/help_SupportName.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_SupportName = $MadelineProto->help->getSupportName();
```

Or, if you're into Lua:

```lua
help_SupportName = help.getSupportName({})
```

