# account.getSavedRingtones

> Fetch saved notification sounds

[Back to methods index](index.html)



Fetch saved notification sounds

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). | Optional|


### Return type: [account.SavedRingtones](/API_docs/types/account.SavedRingtones.html)

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

$account_SavedRingtones = $MadelineProto->account->getSavedRingtones(hash: [$long\|string, $long\|string], );
```
