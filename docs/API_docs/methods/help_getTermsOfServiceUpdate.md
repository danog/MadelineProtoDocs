---
title: help.getTermsOfServiceUpdate
description: Get updated TOS
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getTermsOfServiceUpdate  
[Back to methods index](index.md)


Get updated TOS



### Return type: [help\_TermsOfServiceUpdate](../types/help_TermsOfServiceUpdate.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_TermsOfServiceUpdate = $MadelineProto->help->getTermsOfServiceUpdate();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.getTermsOfServiceUpdate
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getTermsOfServiceUpdate`

Parameters:




Or, if you're into Lua:

```
help_TermsOfServiceUpdate = help.getTermsOfServiceUpdate({})
```

