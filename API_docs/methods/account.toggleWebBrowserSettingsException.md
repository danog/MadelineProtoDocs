# account.toggleWebBrowserSettingsException

> account.toggleWebBrowserSettingsException parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|delete|[Bool](/API_docs/types/Bool.html) | Optional|
|open\_external\_browser|[Bool](/API_docs/types/Bool.html) | Optional|
|url|[string](/API_docs/types/string.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->account->toggleWebBrowserSettingsException(delete: $Bool, open_external_browser: $Bool, url: 'string', );
```
