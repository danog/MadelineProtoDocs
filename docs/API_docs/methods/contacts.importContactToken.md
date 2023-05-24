---
title: "contacts.importContactToken"
description: "Obtain user info from a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_importContactToken.html
---
# Method: contacts.importContactToken
[Back to methods index](index.html)



Obtain user info from a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[string](/API_docs/types/string.html) | The token extracted from the [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links). | Yes|


### Return type: [User](/API_docs/types/User.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->contacts->importContactToken(token: 'string', );
```

