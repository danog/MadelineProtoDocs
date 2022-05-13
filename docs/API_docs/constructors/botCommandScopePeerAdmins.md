---
title: "botCommandScopePeerAdmins"
description: "The specified bot commands will be valid for all admins of the specified group or supergroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommandScopePeerAdmins  
[Back to constructors index](/API_docs/constructors/index.html)



The specified bot commands will be valid for all admins of the specified [group or supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[InputPeer](/API_docs/types/InputPeer.html) | Optional|The chat|



### Type: [BotCommandScope](/API_docs/types/BotCommandScope.html)


### Example:

```
$botCommandScopePeerAdmins = ['_' => 'botCommandScopePeerAdmins', 'peer' => InputPeer];
```  
