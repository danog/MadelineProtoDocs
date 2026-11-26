# account.getReactionsNotifySettings

> Get the current [reaction notification settings »](https://core.telegram.org/api/reactions#notifications-about-reactions).

[Back to methods index](index.html)



Get the current [reaction notification settings »](https://core.telegram.org/api/reactions#notifications-about-reactions).



### Return type: [ReactionsNotifySettings](/API_docs/types/ReactionsNotifySettings.html)

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

$ReactionsNotifySettings = $MadelineProto->account->getReactionsNotifySettings();
```
