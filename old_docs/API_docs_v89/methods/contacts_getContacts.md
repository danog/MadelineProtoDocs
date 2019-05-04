---
title: contacts.getContacts
description: Get all contacts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.getContacts  
[Back to methods index](index.md)


Get all contacts

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | User IDs of previously cached contacts | Optional|


### Return type: [contacts\_Contacts](../types/contacts_Contacts.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_Contacts = $MadelineProto->contacts->getContacts(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
contacts_Contacts = contacts.getContacts({hash={int}, })
```

