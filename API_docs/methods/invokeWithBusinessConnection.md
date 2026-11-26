# invokeWithBusinessConnection

> Invoke a method using a [Telegram Business Bot connection, see here » for more info, including a list of the methods that can be wrapped in this constructor](https://core.telegram.org/api/bots/connected-business-bots).

[Back to methods index](index.html)



Invoke a method using a [Telegram Business Bot connection, see here » for more info, including a list of the methods that can be wrapped in this constructor](https://core.telegram.org/api/bots/connected-business-bots).

Make sure to always send queries wrapped in a `invokeWithBusinessConnection` to the datacenter ID, specified in the `dc_id` field of the [botBusinessConnection](../constructors/botBusinessConnection.html) that is being used.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|connection\_id|[string](/API_docs/types/string.html) | Business connection ID. | Optional|
|query|[!X](/API_docs/types/!X.html) | The actual query. | Yes|


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

$X = $MadelineProto->invokeWithBusinessConnection(connection_id: 'string', query: $!X, );
```
