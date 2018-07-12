---
title: account.finishTakeoutSession
description: Finish account exporting session
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.finishTakeoutSession  
[Back to methods index](index.md)


Finish account exporting session

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|success|[Bool](../types/Bool.md) | Optional|Did the data export succeed?|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->finishTakeoutSession(['success' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.finishTakeoutSession
* params - `{"success": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.finishTakeoutSession`

Parameters:

success - Json encoded Bool




Or, if you're into Lua:

```
Bool = account.finishTakeoutSession({success=Bool, })
```

