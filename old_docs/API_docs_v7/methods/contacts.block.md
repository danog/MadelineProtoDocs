---
title: contacts.block
description: Adds the user to the blacklist.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_block.html
---
# Method: contacts.block
[Back to methods index](index.md)



Adds the user to the blacklist.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User ID | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->contacts->block(['id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
Bool = contacts.block({id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONTACT_ID_INVALID|The provided contact ID is invalid|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|


