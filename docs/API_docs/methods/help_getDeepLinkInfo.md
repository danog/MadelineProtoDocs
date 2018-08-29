---
title: help.getDeepLinkInfo
description: Get deep link info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getDeepLinkInfo  
[Back to methods index](index.md)


Get deep link info

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|path|[string](../types/string.md) | Deep link | Yes|


### Return type: [help\_DeepLinkInfo](../types/help_DeepLinkInfo.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_DeepLinkInfo = $MadelineProto->help->getDeepLinkInfo(['path' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.getDeepLinkInfo
* params - `{"path": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getDeepLinkInfo`

Parameters:

path - Json encoded string




Or, if you're into Lua:

```
help_DeepLinkInfo = help.getDeepLinkInfo({path='string', })
```

