---
title: contacts.getContactIDs
description: Get contacts by IDs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.getContactIDs  
[Back to methods index](index.md)


Get contacts by IDs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | Previously fetched IDs | Optional|


### Return type: [Vector\_of\_int](../types/int.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_int = $MadelineProto->contacts->getContactIDs(['hash' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - contacts.getContactIDs
* params - `{"hash": [int], }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/contacts.getContactIDs`

Parameters:

hash - Json encoded  array of int




Or, if you're into Lua:

```lua
Vector_of_int = contacts.getContactIDs({hash={int}, })
```

