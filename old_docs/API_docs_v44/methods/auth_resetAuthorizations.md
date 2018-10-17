---
title: auth.resetAuthorizations
description: Delete all logged-in sessions.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.resetAuthorizations  
[Back to methods index](index.md)


Delete all logged-in sessions.



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->resetAuthorizations();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/auth.resetAuthorizations`

Parameters:




Or, if you're into Lua:

```lua
Bool = auth.resetAuthorizations({})
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|Timeout|A timeout occurred while fetching data from the bot|


