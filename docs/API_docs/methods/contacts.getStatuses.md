---
title: "contacts.getStatuses"
description: "Use this method to obtain the online statuses of all contacts with an accessible Telegram account."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getStatuses.html
---
# Method: contacts.getStatuses
[Back to methods index](index.html)



Use this method to obtain the online statuses of all contacts with an accessible Telegram account.



### Return type: [Vector\_of\_ContactStatus](/API_docs/types/ContactStatus.html)

### Can userbots use this method: **YES**

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

