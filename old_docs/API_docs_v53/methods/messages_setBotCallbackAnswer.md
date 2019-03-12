---
title: messages.setBotCallbackAnswer
description: Bots only: set the callback answer (after a button was clicked)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.setBotCallbackAnswer  
[Back to methods index](index.md)


Bots only: set the callback answer (after a button was clicked)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|alert|[Bool](../types/Bool.md) | Is this an alert? | Optional|
|query\_id|[long](../types/long.md) | The query ID | Yes|
|message|[string](../types/string.md) | The message | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->setBotCallbackAnswer(['alert' => Bool, 'query_id' => long, 'message' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.setBotCallbackAnswer
* params - `{"alert": Bool, "query_id": long, "message": "string", }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.setBotCallbackAnswer`

Parameters:

alert - Json encoded Bool

query_id - Json encoded long

message - Json encoded string




Or, if you're into Lua:

```lua
Bool = messages.setBotCallbackAnswer({alert=Bool, query_id=long, message='string', })
```


## Return value 

If the length of the provided message is bigger than 4096, the message will be split in chunks and the method will be called multiple times, with the same parameters (except for the message), and an array of [Bool](../types/Bool.md) will be returned instead.


### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|QUERY_ID_INVALID|The query ID is invalid|


