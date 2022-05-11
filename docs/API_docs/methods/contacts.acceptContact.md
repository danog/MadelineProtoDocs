---
title: "contacts.acceptContact"
description: "If the [peer settings](../constructors/peerSettings.html) of a new user allow us to add them as contact, add that user as contact"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/contacts_acceptContact.html
---
# Method: contacts.acceptContact
[Back to methods index](index.html)



If the [peer settings](../constructors/peerSettings.html) of a new user allow us to add them as contact, add that user as contact

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user to add as contact | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->contacts->acceptContact(id: InputUser, );
```

