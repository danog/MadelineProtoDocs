# account.setGlobalPrivacySettings

> Set global privacy settings

[Back to methods index](index.html)



Set global privacy settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|settings|[GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html) | Global privacy settings | Yes|


### Return type: [GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$GlobalPrivacySettings = $MadelineProto->account->setGlobalPrivacySettings(settings: $GlobalPrivacySettings, );
```
