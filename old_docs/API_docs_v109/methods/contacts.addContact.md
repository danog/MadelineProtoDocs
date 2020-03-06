---
title: contacts.addContact
description: Add an existing telegram user as contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_addContact.html
---
# Method: contacts.addContact  
[Back to methods index](index.md)


Add an existing telegram user as contact

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|add\_phone\_privacy\_exception|[Bool](../types/Bool.md) | Allow the other user to see our phone number? | Optional|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Telegram ID of the other user | Optional|
|first\_name|[string](../types/string.md) | First name | Yes|
|last\_name|[string](../types/string.md) | Last name | Yes|
|phone|[string](../types/string.md) | User's phone number | Yes|


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


