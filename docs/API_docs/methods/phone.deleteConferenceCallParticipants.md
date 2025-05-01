---
title: "phone.deleteConferenceCallParticipants"
description: "phone.deleteConferenceCallParticipants parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_deleteConferenceCallParticipants.html
---
# Method: phone.deleteConferenceCallParticipants
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|only\_left|[Bool](/API_docs/types/Bool.html) | Optional|
|kick|[Bool](/API_docs/types/Bool.html) | Optional|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|ids|Array of [long](/API_docs/types/long.html) | Yes|
|block|[bytes](/API_docs/types/bytes.html) | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->phone->deleteConferenceCallParticipants(only_left: $Bool, kick: $Bool, call: $InputGroupCall, ids: [$long, $long], block: 'bytes', );
```

