---
title: "phone.setCallRating"
description: "Rate a call"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/phone_setCallRating.html
---
# Method: phone.setCallRating
[Back to methods index](index.html)



Rate a call

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_initiative|[Bool](/API_docs/types/Bool.html) | Whether the user decided on their own initiative to rate the call | Optional|
|peer|[InputPhoneCall](/API_docs/types/InputPhoneCall.html) | The call to rate | Yes|
|rating|[int](/API_docs/types/int.html) | Rating in `1-5` stars | Yes|
|comment|[string](/API_docs/types/string.html) | An additional comment | Yes|


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
$Updates = $MadelineProto->phone->setCallRating(user_initiative: Bool, peer: InputPhoneCall, rating: int, comment: 'string', );
```

