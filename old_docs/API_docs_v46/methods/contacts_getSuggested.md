---
title: contacts.getSuggested
description: Get suggested contacts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.getSuggested  
[Back to methods index](index.md)


Get suggested contacts

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [contacts\_Suggested](../types/contacts_Suggested.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_Suggested = $MadelineProto->contacts->getSuggested(['limit' => int, ]);
```

Or, if you're into Lua:

```lua
contacts_Suggested = contacts.getSuggested({limit=int, })
```

