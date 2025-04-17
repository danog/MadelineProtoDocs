---
title: "contacts.getSponsoredPeers"
description: "contacts.getSponsoredPeers parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_getSponsoredPeers.html
---
# Method: contacts.getSponsoredPeers
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|q|[string](/API_docs/types/string.html) | Optional|


### Return type: [contacts.SponsoredPeers](/API_docs/types/contacts.SponsoredPeers.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$contacts_SponsoredPeers = $MadelineProto->contacts->getSponsoredPeers(q: 'string', );
```

