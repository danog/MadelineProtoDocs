---
title: contacts.resetSaved
description: Reset saved contacts
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.resetSaved  
[Back to methods index](index.md)


Reset saved contacts



### Return type: [Bool](../types/Bool.md)

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

$Bool = $MadelineProto->contacts->resetSaved();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - contacts.resetSaved
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/contacts.resetSaved`

Parameters:




Or, if you're into Lua:

```lua
Bool = contacts.resetSaved({})
```

