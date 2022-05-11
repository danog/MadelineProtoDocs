---
title: "contacts.resolveUsername"
description: "You cannot use this method directly, use the resolveUsername, getPwrChat, getInfo, getFullInfo methods instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_resolveUsername.html
---
# Method: contacts.resolveUsername
[Back to methods index](index.html)



You cannot use this method directly, use the resolveUsername, getPwrChat, getInfo, getFullInfo methods instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|username|[string](/API_docs/types/string.html) | @username to resolve | Yes|


### Return type: [contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$contacts_ResolvedPeer = $MadelineProto->contacts->resolveUsername(username: 'string', );
```

