---
title: "channels.createChannel"
description: "Create a [supergroup/channel](https://core.telegram.org/api/channel)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_createChannel.html
---
# Method: channels.createChannel
[Back to methods index](index.md)



Create a [supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Bool](/API_docs/types/Bool.md) | Whether to create a [channel](https://core.telegram.org/api/channel) | Optional|
|megagroup|[Bool](/API_docs/types/Bool.md) | Whether to create a [supergroup](https://core.telegram.org/api/channel) | Optional|
|for\_import|[Bool](/API_docs/types/Bool.md) |  | Optional|
|title|[string](/API_docs/types/string.md) | Channel title | Yes|
|about|[string](/API_docs/types/string.md) | Channel description | Yes|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.md) | Geogroup location | Optional|
|address|[string](/API_docs/types/string.md) | Geogroup address | Optional|


### Return type: [Updates](/API_docs/types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->createChannel(['broadcast' => Bool, 'megagroup' => Bool, 'for_import' => Bool, 'title' => 'string', 'about' => 'string', 'geo_point' => InputGeoPoint, 'address' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNELS_ADMIN_LOCATED_TOO_MUCH|The user has reached the limit of public geogroups|
|400|CHANNELS_TOO_MUCH|You have joined too many channels/supergroups|
|400|CHAT_ABOUT_TOO_LONG|Chat about too long|
|400|CHAT_TITLE_EMPTY|No chat title provided|
|400|INPUT_REQUEST_TOO_LONG|The request is too big|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|406|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|403|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


