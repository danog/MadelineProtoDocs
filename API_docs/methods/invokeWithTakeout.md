# invokeWithTakeout

> Invoke a method within a [takeout session, see here » for more info](https://core.telegram.org/api/takeout).

[Back to methods index](index.html)



Invoke a method within a [takeout session, see here » for more info](https://core.telegram.org/api/takeout).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|takeout\_id|[long](/API_docs/types/long.html) | [Takeout session ID »](https://core.telegram.org/api/takeout) | Yes|
|query|[!X](/API_docs/types/!X.html) | Query | Yes|


### Return type: [X](/API_docs/types/X.html)

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

$X = $MadelineProto->invokeWithTakeout(takeout_id: $long, query: $!X, );
```
