# stats.getPollStats

> stats.getPollStats parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Optional|


### Return type: [stats.PollStats](/API_docs/types/stats.PollStats.html)

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

$stats_PollStats = $MadelineProto->stats->getPollStats(dark: $Bool, peer: $InputPeer, msg_id: $int, );
```
