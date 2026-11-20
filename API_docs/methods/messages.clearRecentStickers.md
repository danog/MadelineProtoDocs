# messages.clearRecentStickers

> Clear recent stickers

[Back to methods index](index.html)



Clear recent stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|attached|[Bool](/API_docs/types/Bool.html) | Set this flag to clear the list of stickers recently attached to photo or video files | Optional|


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

$Bool = $MadelineProto->messages->clearRecentStickers(attached: $Bool, );
```
