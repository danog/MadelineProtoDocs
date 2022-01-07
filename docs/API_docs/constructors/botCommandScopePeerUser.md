---
title: "botCommandScopePeerUser"
description: "botCommandScopePeerUser attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommandScopePeerUser  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputPeer](/API_docs/types/InputPeer.md) | Optional|
|user\_id|[InputUser](/API_docs/types/InputUser.md) | Optional|



### Type: [BotCommandScope](/API_docs/types/BotCommandScope.md)


### Example:

```php
$botCommandScopePeerUser = ['_' => 'botCommandScopePeerUser', 'peer' => InputPeer, 'user_id' => InputUser];
```  
