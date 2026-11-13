# smsjobs.getStatus

> Get SMS jobs status (official clients only).

[Back to methods index](index.html)



Get SMS jobs status (official clients only).



### Return type: [smsjobs.Status](/API_docs/types/smsjobs.Status.html)

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

$smsjobs_Status = $MadelineProto->smsjobs->getStatus();
```
