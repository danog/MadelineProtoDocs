---
title: req_pq_multi
description: Requests PQ for factorization (new version)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: req\_pq\_multi  
[Back to methods index](index.md)


Requests PQ for factorization (new version)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|nonce|[int128](../types/int128.md) | Random number for cryptographic security | Yes|


### Return type: [ResPQ](../types/ResPQ.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ResPQ = $MadelineProto->req_pq_multi(['nonce' => int128, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - req_pq_multi
* params - `{"nonce": int128, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/req_pq_multi`

Parameters:

nonce - Json encoded int128




Or, if you're into Lua:

```lua
ResPQ = req_pq_multi({nonce=int128, })
```

