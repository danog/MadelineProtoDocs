---
title: messages.createChannel
description: Create channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.createChannel  
[Back to methods index](index.md)


Create channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|title|[string](../types/string.md) | Channel/supergroup title | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->createChannel(['title' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.createChannel({title='string', })
```

