---
title: contacts.deleteContact
description: Delete a contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_deleteContact.html
---
# Method: contacts.deleteContact  
[Back to methods index](index.md)


Delete a contact

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The contact to delete | Optional|


### Return type: [contacts.Link](../types/contacts.Link.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts.Link = $MadelineProto->contacts->deleteContact(['id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
contacts.Link = contacts.deleteContact({id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONTACT_ID_INVALID|The provided contact ID is invalid|


