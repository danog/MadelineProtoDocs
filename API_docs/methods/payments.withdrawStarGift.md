# payments.withdrawStarGift

> payments.withdrawStarGift parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|keep\_on\_profile|[Bool](/API_docs/types/Bool.html) | Optional|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Yes|
|tmp\_password|[bytes](/API_docs/types/bytes.html) | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->payments->withdrawStarGift(keep_on_profile: $Bool, stargift: $InputSavedStarGift, tmp_password: 'bytes', );
```
