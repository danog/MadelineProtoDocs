---
title: "contacts.exportNoPaidMessagesToken"
description: "contacts.exportNoPaidMessagesToken parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_exportNoPaidMessagesToken.html
---
# Method: contacts.exportNoPaidMessagesToken
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|revoke|[Bool](/API_docs/types/Bool.html) | Optional|
|temporary|[Bool](/API_docs/types/Bool.html) | Optional|


### Return type: [ExportedNoPaidMessagesToken](/API_docs/types/ExportedNoPaidMessagesToken.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedNoPaidMessagesToken = $MadelineProto->contacts->exportNoPaidMessagesToken(revoke: $Bool, temporary: $Bool, );
```

