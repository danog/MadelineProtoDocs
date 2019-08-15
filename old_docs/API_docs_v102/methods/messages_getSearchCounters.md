---
title: messages.getSearchCounters
description: Get search counter
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getSearchCounters  
[Back to methods index](index.md)


Get search counter

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|filters|Array of [MessagesFilter](../types/MessagesFilter.md) | Filters | Yes|


### Return type: [Vector\_of\_messages\_SearchCounter](../types/messages_SearchCounter.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_messages_SearchCounter = $MadelineProto->messages->getSearchCounters(['peer' => InputPeer, 'filters' => [MessagesFilter, MessagesFilter], ]);
```

Or, if you're into Lua:

```lua
Vector_of_messages_SearchCounter = messages.getSearchCounters({peer=InputPeer, filters={MessagesFilter}, })
```

