---
title: contacts.getTopPeers
description: Get most used chats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: contacts.getTopPeers  
[Back to methods index](index.md)


Get most used chats

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|correspondents|[Bool](../types/Bool.md) | Fetch users? | Optional|
|bots\_pm|[Bool](../types/Bool.md) | Fetch bots? | Optional|
|bots\_inline|[Bool](../types/Bool.md) | Fetch inline bots? | Optional|
|phone\_calls|[Bool](../types/Bool.md) | Fetch phone calls? | Optional|
|groups|[Bool](../types/Bool.md) | Fetch groups? | Optional|
|channels|[Bool](../types/Bool.md) | Fetch channels and supergroups? | Optional|
|offset|[int](../types/int.md) | Initially 0, then `$offset += $contacts_TopPeers['categories']['count'];` | Yes|
|limit|[int](../types/int.md) | How many results to fetch | Yes|
|hash|[int](../types/int.md) | $MadelineProto->gen_vector_hash(previously fetched peer ids); | Yes|


### Return type: [contacts\_TopPeers](../types/contacts_TopPeers.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_TopPeers = $MadelineProto->contacts->getTopPeers(['correspondents' => Bool, 'bots_pm' => Bool, 'bots_inline' => Bool, 'phone_calls' => Bool, 'groups' => Bool, 'channels' => Bool, 'offset' => int, 'limit' => int, 'hash' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/contacts.getTopPeers`

Parameters:

correspondents - Json encoded Bool

bots_pm - Json encoded Bool

bots_inline - Json encoded Bool

phone_calls - Json encoded Bool

groups - Json encoded Bool

channels - Json encoded Bool

offset - Json encoded int

limit - Json encoded int

hash - Json encoded int




Or, if you're into Lua:

```
contacts_TopPeers = contacts.getTopPeers({correspondents=Bool, bots_pm=Bool, bots_inline=Bool, phone_calls=Bool, groups=Bool, channels=Bool, offset=int, limit=int, hash=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|TYPES_EMPTY|The types field is empty|


