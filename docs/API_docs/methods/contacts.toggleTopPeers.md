---
title: "contacts.toggleTopPeers"
description: "Enable/disable [top peers](https://core.telegram.org/api/top-rating)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_toggleTopPeers.html
---
# Method: contacts.toggleTopPeers
[Back to methods index](index.html)



Enable/disable [top peers](https://core.telegram.org/api/top-rating)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|enabled|[Bool](/API_docs/types/Bool.html) | Enable/disable | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->contacts->toggleTopPeers(enabled: $Bool, );
```

