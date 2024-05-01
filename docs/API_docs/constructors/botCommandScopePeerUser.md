---
title: "botCommandScopePeerUser"
description: "The specified bot commands will be valid only for a specific user in the specified group or supergroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommandScopePeerUser  
[Back to constructors index](/API_docs/constructors/index.html)



The specified bot commands will be valid only for a specific user in the specified [group or supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[InputPeer](/API_docs/types/InputPeer.html) | Optional|The chat|
|user\_id|[InputUser](/API_docs/types/InputUser.html) | Optional|The user|



### Type: [BotCommandScope](/API_docs/types/BotCommandScope.html)


### Example:

```
$botCommandScopePeerUser = ['_' => 'botCommandScopePeerUser', 'peer' => InputPeer, 'user_id' => InputUser];
```  
