---
title: "contacts.resolvePhone"
description: "Resolve a phone number to get user info, if their privacy settings allow it."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_resolvePhone.html
---
# Method: contacts.resolvePhone
[Back to methods index](index.html)



Resolve a phone number to get user info, if their privacy settings allow it.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone|[string](/API_docs/types/string.html) | Phone number in international format, possibly obtained from a `t.me/+number` or `tg://resolve?phone=number` URI. | Yes|


### Return type: [contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$contacts_ResolvedPeer = $MadelineProto->contacts->resolvePhone(phone: 'string', );
```

