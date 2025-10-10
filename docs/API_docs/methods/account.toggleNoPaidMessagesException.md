---
title: "account.toggleNoPaidMessagesException"
description: "Allow a user to send us messages without paying if [paid messages »](https://core.telegram.org/api/paid-messages) are enabled."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_toggleNoPaidMessagesException.html
---
# Method: account.toggleNoPaidMessagesException
[Back to methods index](index.html)



Allow a user to send us messages without paying if [paid messages »](https://core.telegram.org/api/paid-messages) are enabled.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|refund\_charged|[Bool](/API_docs/types/Bool.html) | If set and `require_payment` is not set, refunds the amounts the user has already paid us to send us messages (directly or via a monoforum). | Optional|
|require\_payment|[Bool](/API_docs/types/Bool.html) | If set, requires the user to pay in order to send us messages. <br>Can only be **set** by monoforums, not users, i.e. `parent_peer` must be set if this flag is set; users must instead use the [inputPrivacyKeyNoPaidMessages](../constructors/inputPrivacyKeyNoPaidMessages.html) privacy setting to remove a previously added exemption. <br>If not set, allows the user to send us messages without paying (can be **unset** by both monoforums and users). | Optional|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, applies the setting within the [monoforum aka direct messages »](https://core.telegram.org/api/monoforum) (pass the ID of the monoforum, **not** the ID of the associated channel). | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | The user to exempt or unexempt. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->toggleNoPaidMessagesException(refund_charged: $Bool, require_payment: $Bool, parent_peer: $InputPeer, user_id: $InputUser, );
```

