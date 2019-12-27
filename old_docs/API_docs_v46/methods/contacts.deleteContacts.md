---
title: contacts.deleteContacts
description: Deletes several contacts from the list.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.deleteContacts  
[Back to methods index](index.md)


Deletes several contacts from the list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The contacts to delete | Yes|


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

$Bool = $MadelineProto->contacts->deleteContacts(['id' => [InputUser, InputUser], ]);
```

Or, if you're into Lua:

```lua
Bool = contacts.deleteContacts({id={InputUser}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|-503|Timeout|Timeout while fetching data|


