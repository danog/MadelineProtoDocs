# account.saveTheme

> Save a theme

[Back to methods index](index.html)



Save a theme

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|theme|[InputTheme](/API_docs/types/InputTheme.html) | Theme to save | Yes|
|unsave|[Bool](/API_docs/types/Bool.html) | Unsave | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->account->saveTheme(theme: $InputTheme, unsave: $Bool, );
```
