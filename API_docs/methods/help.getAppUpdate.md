# help.getAppUpdate

> Returns information on update availability for the current application.

[Back to methods index](index.html)



Returns information on update availability for the current application.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|source|[string](/API_docs/types/string.html) | Source | Optional|


### Return type: [help.AppUpdate](/API_docs/types/help.AppUpdate.html)

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

$help_AppUpdate = $MadelineProto->help->getAppUpdate(source: 'string', );
```
