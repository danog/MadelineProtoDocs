---
title: "attachMenuBot"
description: "attachMenuBot attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBot  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|
|has\_settings|[Bool](/API_docs/types/Bool.html) | Optional|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|short\_name|[string](/API_docs/types/string.html) | Yes|
|peer\_types|Array of [AttachMenuPeerType](/API_docs/types/AttachMenuPeerType.html) | Yes|
|icons|Array of [AttachMenuBotIcon](/API_docs/types/AttachMenuBotIcon.html) | Yes|



### Type: [AttachMenuBot](/API_docs/types/AttachMenuBot.html)


### Example:

```
$attachMenuBot = ['_' => 'attachMenuBot', 'inactive' => Bool, 'has_settings' => Bool, 'bot_id' => long, 'short_name' => 'string', 'peer_types' => [AttachMenuPeerType, AttachMenuPeerType], 'icons' => [AttachMenuBotIcon, AttachMenuBotIcon]];
```  
