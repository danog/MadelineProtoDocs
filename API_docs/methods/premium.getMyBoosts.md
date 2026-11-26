# premium.getMyBoosts

> Obtain which peers are we currently [boosting](https://core.telegram.org/api/boost), and how many [boost slots](https://core.telegram.org/api/boost) we have left.

[Back to methods index](index.html)



Obtain which peers are we currently [boosting](https://core.telegram.org/api/boost), and how many [boost slots](https://core.telegram.org/api/boost) we have left.



### Return type: [premium.MyBoosts](/API_docs/types/premium.MyBoosts.html)

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

$premium_MyBoosts = $MadelineProto->premium->getMyBoosts();
```
