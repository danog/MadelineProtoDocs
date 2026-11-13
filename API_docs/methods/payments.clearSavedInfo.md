# payments.clearSavedInfo

> Clear saved payment information

[Back to methods index](index.html)



Clear saved payment information

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|credentials|[Bool](/API_docs/types/Bool.html) | Remove saved payment credentials | Optional|
|info|[Bool](/API_docs/types/Bool.html) | Clear the last order settings saved by the user | Optional|


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

$Bool = $MadelineProto->payments->clearSavedInfo(credentials: $Bool, info: $Bool, );
```
