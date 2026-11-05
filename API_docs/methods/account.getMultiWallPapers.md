# account.getMultiWallPapers

> Get info about multiple [wallpapers](https://core.telegram.org/api/wallpapers)

[Back to methods index](index.html)



Get info about multiple [wallpapers](https://core.telegram.org/api/wallpapers)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|wallpapers|Array of [InputWallPaper](/API_docs/types/InputWallPaper.html) | [Wallpapers](https://core.telegram.org/api/wallpapers) to fetch info about | Yes|


### Return type: [Vector\_of\_WallPaper](/API_docs/types/WallPaper.html)

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

$Vector_of_WallPaper = $MadelineProto->account->getMultiWallPapers(wallpapers: [$InputWallPaper, $InputWallPaper], );
```
