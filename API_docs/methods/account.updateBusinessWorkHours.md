# account.updateBusinessWorkHours

> Specify a set of [Telegram Business opening hours](https://core.telegram.org/api/business#opening-hours).  

[Back to methods index](index.html)



Specify a set of [Telegram Business opening hours](https://core.telegram.org/api/business#opening-hours).  
This info will be contained in [userFull](../constructors/userFull.html).`business_work_hours`.

To remove all opening hours, invoke the method without setting the `business_work_hours` field.

Note that the opening hours specified by the user must be appropriately validated and transformed before invoking the method, as specified [here »](https://core.telegram.org/api/business#opening-hours).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|business\_work\_hours|[BusinessWorkHours](/API_docs/types/BusinessWorkHours.html) | Opening hours (optional, if not set removes all opening hours). | Optional|


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

$Bool = $MadelineProto->account->updateBusinessWorkHours(business_work_hours: $BusinessWorkHours, );
```
