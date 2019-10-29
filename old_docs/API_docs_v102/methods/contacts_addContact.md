---
title: contacts.addContact
description: Add contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.addContact  
[Back to methods index](index.md)


Add contact

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|add\_phone\_privacy\_exception|[Bool](../types/Bool.md) | Phone privacy exception? | Optional|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | ID | Optional|
|first\_name|[string](../types/string.md) | First name | Yes|
|last\_name|[string](../types/string.md) | Last name | Yes|
|phone|[string](../types/string.md) | Phone number | Yes|


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

$Updates = $MadelineProto->contacts->addContact(['add_phone_privacy_exception' => Bool, 'id' => InputUser, 'first_name' => 'string', 'last_name' => 'string', 'phone' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = contacts.addContact({add_phone_privacy_exception=Bool, id=InputUser, first_name='string', last_name='string', phone='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONTACT_ID_INVALID|The provided contact ID is invalid|
|400|CONTACT_NAME_EMPTY|Contact name empty|


