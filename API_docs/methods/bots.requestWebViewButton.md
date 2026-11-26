# bots.requestWebViewButton

> bots.requestWebViewButton parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|button|[KeyboardButton](/API_docs/types/KeyboardButton.html) | Yes|


### Return type: [bots.RequestedButton](/API_docs/types/bots.RequestedButton.html)

### Can users use this method: **NO**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$bots_RequestedButton = $MadelineProto->bots->requestWebViewButton(user_id: $InputUser, button: $KeyboardButton, );
```
