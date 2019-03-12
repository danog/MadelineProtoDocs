---
title: contacts.resetTopPeerRating
description: Reset top peer rating for a certain category/peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.resetTopPeerRating  
[Back to methods index](index.md)


Reset top peer rating for a certain category/peer

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|category|[TopPeerCategory](../types/TopPeerCategory.md) | The category  | Yes|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The peer | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->contacts->resetTopPeerRating(['category' => TopPeerCategory, 'peer' => InputPeer, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/contacts.resetTopPeerRating`

Parameters:

category - Json encoded TopPeerCategory

peer - Json encoded InputPeer




Or, if you're into Lua:

```lua
Bool = contacts.resetTopPeerRating({category=TopPeerCategory, peer=InputPeer, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


