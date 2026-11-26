# phone.getGroupCallStreamRtmpUrl

> Get RTMP URL and stream key for RTMP livestreams. Can be used even before creating the actual RTMP livestream with [phone.createGroupCall](../methods/phone.createGroupCall.html) (the `rtmp_stream` flag must be set).

[Back to methods index](index.html)



Get RTMP URL and stream key for RTMP livestreams. Can be used even before creating the actual RTMP livestream with [phone.createGroupCall](../methods/phone.createGroupCall.html) (the `rtmp_stream` flag must be set).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|live\_story|[Bool](/API_docs/types/Bool.html) |  | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer to livestream into | Optional|
|revoke|[Bool](/API_docs/types/Bool.html) | Whether to revoke the previous stream key or simply return the existing one | Yes|


### Return type: [phone.GroupCallStreamRtmpUrl](/API_docs/types/phone.GroupCallStreamRtmpUrl.html)

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

$phone_GroupCallStreamRtmpUrl = $MadelineProto->phone->getGroupCallStreamRtmpUrl(live_story: $Bool, peer: $InputPeer, revoke: $Bool, );
```
