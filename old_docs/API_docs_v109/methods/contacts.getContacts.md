---
title: contacts.getContacts
description: Returns the current user's contact list.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getContacts.html
---
# Method: contacts.getContacts  
[Back to methods index](index.md)


Returns the current user's contact list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | User IDs of previously cached contacts | Optional|


### Return type: [contacts.Contacts](../types/contacts.Contacts.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts.Contacts = $MadelineProto->contacts->getContacts(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
contacts.Contacts = contacts.getContacts({hash={int}, })
```

