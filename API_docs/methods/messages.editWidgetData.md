# messages.editWidgetData

> messages.editWidgetData parameters, return type and example

[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|widget\_id|[long](/API_docs/types/long.html) | Yes|
|public\_data|[string](/API_docs/types/string.html) | Optional|
|cache\_time|[int](/API_docs/types/int.html) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


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

$Bool = $MadelineProto->messages->editWidgetData(widget_id: $long, public_data: 'string', cache_time: $int, );
```
