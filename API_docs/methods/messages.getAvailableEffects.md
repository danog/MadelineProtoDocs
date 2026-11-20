# messages.getAvailableEffects

> Fetch the full list of usable [animated message effects »](https://core.telegram.org/api/effects).

[Back to methods index](index.html)



Fetch the full list of usable [animated message effects »](https://core.telegram.org/api/effects).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [messages.AvailableEffects](/API_docs/types/messages.AvailableEffects.html)

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

$messages_AvailableEffects = $MadelineProto->messages->getAvailableEffects(hash: [$long\|string, $long\|string], );
```
