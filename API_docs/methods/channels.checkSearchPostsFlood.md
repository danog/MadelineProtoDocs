# channels.checkSearchPostsFlood

> Check if the specified [global post search »](https://core.telegram.org/api/search#posts-tab) requires payment.

[Back to methods index](index.html)



Check if the specified [global post search »](https://core.telegram.org/api/search#posts-tab) requires payment.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|query|[string](/API_docs/types/string.html) | The query. | Optional|


### Return type: [SearchPostsFlood](/API_docs/types/SearchPostsFlood.html)

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

$SearchPostsFlood = $MadelineProto->channels->checkSearchPostsFlood(query: 'string', );
```
