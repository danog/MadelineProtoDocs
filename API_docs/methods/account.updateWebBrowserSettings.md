# account.updateWebBrowserSettings

> account.updateWebBrowserSettings parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|open\_external\_browser|[Bool](/API_docs/types/Bool.html) | Optional|
|display\_close\_button|[Bool](/API_docs/types/Bool.html) | Optional|


### Return type: [account.WebBrowserSettings](/API_docs/types/account.WebBrowserSettings.html)

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

$account_WebBrowserSettings = $MadelineProto->account->updateWebBrowserSettings(open_external_browser: $Bool, display_close_button: $Bool, );
```
