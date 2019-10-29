---
title: contacts.acceptContact
description: Accept contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.acceptContact  
[Back to methods index](index.md)


Accept contact

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | ID | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->contacts->acceptContact(['id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
Updates = contacts.acceptContact({id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONTACT_REQ_MISSING|Missing contact request|


