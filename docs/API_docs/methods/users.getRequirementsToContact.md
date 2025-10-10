---
title: "users.getRequirementsToContact"
description: "Check whether we can write to the specified users, used to implement bulk checks for [Premium-only messages »](https://core.telegram.org/api/privacy#require-premium-for-new-non-contact-users) and [paid messages »](https://core.telegram.org/api/paid-messages)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/users_getRequirementsToContact.html
---
# Method: users.getRequirementsToContact
[Back to methods index](index.html)



Check whether we can write to the specified users, used to implement bulk checks for [Premium-only messages »](https://core.telegram.org/api/privacy#require-premium-for-new-non-contact-users) and [paid messages »](https://core.telegram.org/api/paid-messages).

For each input user, returns a [RequirementToContact](../types/RequirementToContact.html) constructor (at the same offset in the vector) containing requirements to contact them.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Users to check. | Yes|


### Return type: [Vector\_of\_RequirementToContact](/API_docs/types/RequirementToContact.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_RequirementToContact = $MadelineProto->users->getRequirementsToContact(id: [$InputUser, $InputUser], );
```

