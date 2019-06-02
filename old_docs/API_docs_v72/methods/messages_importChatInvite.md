---
title: messages.importChatInvite
description: Import chat invite
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.importChatInvite  
[Back to methods index](index.md)


Import chat invite

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[string](../types/string.md) | The invite link in t.me/joinchat/aflakf format | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->importChatInvite(['hash' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = messages.importChatInvite({hash='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNELS_TOO_MUCH|You have joined too many channels/supergroups|
|INVITE_HASH_EMPTY|The invite hash is empty|
|INVITE_HASH_EXPIRED|The invite link has expired|
|INVITE_HASH_INVALID|The invite hash is invalid|
|USER_ALREADY_PARTICIPANT|The user is already in the group|
|USERS_TOO_MUCH|The maximum number of users has been exceeded (to create a chat, for example)|
|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


