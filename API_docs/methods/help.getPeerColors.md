# help.getPeerColors

> Get the set of [accent color palettes »](https://core.telegram.org/api/colors) that can be used for message accents.

[Back to methods index](index.html)



Get the set of [accent color palettes »](https://core.telegram.org/api/colors) that can be used for message accents.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) |  | Optional|


### Return type: [help.PeerColors](/API_docs/types/help.PeerColors.html)

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

$help_PeerColors = $MadelineProto->help->getPeerColors(hash: [$long\|string, $long\|string], );
```
