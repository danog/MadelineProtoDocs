---
title: messages.getAllChats
description: Get all chats, channels and supergroups
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAllChats.html
---
# Method: messages.getAllChats
[Back to methods index](index.md)



Get all chats, channels and supergroups

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|except\_ids|Array of [int](../types/int.md) | Except these chats/channels/supergroups | Yes|


### Return type: [messages.Chats](../types/messages.Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->messages->getAllChats(['except_ids' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_Chats = messages.getAllChats({except_ids={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


