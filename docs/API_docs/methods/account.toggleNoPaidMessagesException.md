---
title: "account.toggleNoPaidMessagesException"
description: "account.toggleNoPaidMessagesException parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_toggleNoPaidMessagesException.html
---
# Method: account.toggleNoPaidMessagesException
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|refund\_charged|[Bool](/API_docs/types/Bool.html) | Optional|
|require\_payment|[Bool](/API_docs/types/Bool.html) | Optional|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->toggleNoPaidMessagesException(refund_charged: $Bool, require_payment: $Bool, parent_peer: $InputPeer, user_id: $InputUser, );
```

