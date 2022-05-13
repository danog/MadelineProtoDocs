---
title: "botCommandScopePeer"
description: "The specified bot commands will be valid only in a specific dialog."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommandScopePeer  
[Back to constructors index](/API_docs/constructors/index.html)



The specified bot commands will be valid only in a specific dialog.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[InputPeer](/API_docs/types/InputPeer.html) | Optional|The dialog|



### Type: [BotCommandScope](/API_docs/types/BotCommandScope.html)


### Example:

```
$botCommandScopePeer = ['_' => 'botCommandScopePeer', 'peer' => InputPeer];
```  
