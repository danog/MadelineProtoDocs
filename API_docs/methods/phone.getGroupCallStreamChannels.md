# phone.getGroupCallStreamChannels

> Get info about RTMP streams in a group call or livestream.  

[Back to methods index](index.html)



Get info about RTMP streams in a group call or livestream.  
This method should be invoked to the same group/channel-related DC used for [downloading livestream chunks](https://core.telegram.org/api/files#downloading-files).  
As usual, the media DC is preferred, if available.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Group call or livestream | Yes|


### Return type: [phone.GroupCallStreamChannels](/API_docs/types/phone.GroupCallStreamChannels.html)

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

$phone_GroupCallStreamChannels = $MadelineProto->phone->getGroupCallStreamChannels(call: $InputGroupCall, );
```
