---
title: "contacts.exportContactToken"
description: "Generates a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links) for the currently logged-in user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_exportContactToken.html
---
# Method: contacts.exportContactToken
[Back to methods index](index.html)



Generates a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links) for the currently logged-in user.



### Return type: [ExportedContactToken](/API_docs/types/ExportedContactToken.html)

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

$ExportedContactToken = $MadelineProto->contacts->exportContactToken();
```

