# account.getWallPaper

> Get info about a certain [wallpaper](https://core.telegram.org/api/wallpapers)

[Back to methods index](index.html)



Get info about a certain [wallpaper](https://core.telegram.org/api/wallpapers)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|wallpaper|[InputWallPaper](/API_docs/types/InputWallPaper.html) | The [wallpaper](https://core.telegram.org/api/wallpapers) to get info about | Yes|


### Return type: [WallPaper](/API_docs/types/WallPaper.html)

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

$WallPaper = $MadelineProto->account->getWallPaper(wallpaper: $InputWallPaper, );
```
