---
title: messages.getRecentLocations
description: Get recent locations
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getRecentLocations  
[Back to methods index](index.md)


Get recent locations

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where to search locations | Optional|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

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

$messages_Messages = $MadelineProto->messages->getRecentLocations(['peer' => InputPeer, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getRecentLocations({peer=InputPeer, limit=int, })
```

