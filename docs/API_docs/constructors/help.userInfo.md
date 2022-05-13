---
title: "help.userInfo"
description: "Internal use"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_userInfo.html
---
# Constructor: help.userInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Internal use

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[string](/API_docs/types/string.html) | Yes|Info|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|author|[string](/API_docs/types/string.html) | Yes|Author|
|date|[int](/API_docs/types/int.html) | Yes|Date|



### Type: [help.UserInfo](/API_docs/types/help.UserInfo.html)


### Example:

```
$help_userInfo = ['_' => 'help.userInfo', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'author' => 'string', 'date' => int];
```  
