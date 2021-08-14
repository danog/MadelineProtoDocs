---
title: contacts.getStatuses
description: Returns the list of contact statuses.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getStatuses.html
---
# Method: contacts.getStatuses
[Back to methods index](index.md)



Returns the list of contact statuses.



### Return type: [Vector\_of\_ContactStatus](../types/ContactStatus.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_ContactStatus = $MadelineProto->contacts->getStatuses();
```

Or, if you're into Lua:

```lua
Vector_of_ContactStatus = contacts.getStatuses({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


