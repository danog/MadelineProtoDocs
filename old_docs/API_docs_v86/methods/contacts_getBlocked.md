---
title: contacts.getBlocked
description: Get blocked users
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.getBlocked  
[Back to methods index](index.md)


Get blocked users

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | Initially 0, then set to the number of blocked contacts previously fetched | Yes|
|limit|[int](../types/int.md) | How many blocked contacts to fetch | Yes|


### Return type: [contacts\_Blocked](../types/contacts_Blocked.md)

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

$contacts_Blocked = $MadelineProto->contacts->getBlocked(['offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
contacts_Blocked = contacts.getBlocked({offset=int, limit=int, })
```

