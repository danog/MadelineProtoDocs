---
title: contacts.toggleTopPeers
description: Toggle top peers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.toggleTopPeers  
[Back to methods index](index.md)


Toggle top peers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|enabled|[Bool](../types/Bool.md) | Enable or disable top peer | Yes|


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

$Bool = $MadelineProto->contacts->toggleTopPeers(['enabled' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - contacts.toggleTopPeers
* params - `{"enabled": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/contacts.toggleTopPeers`

Parameters:

enabled - Json encoded Bool




Or, if you're into Lua:

```lua
Bool = contacts.toggleTopPeers({enabled=Bool, })
```

