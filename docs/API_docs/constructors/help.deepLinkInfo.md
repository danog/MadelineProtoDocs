---
title: "help.deepLinkInfo"
description: "Deep linking info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_deepLinkInfo.html
---
# Constructor: help.deepLinkInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Deep linking info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update\_app|[Bool](/API_docs/types/Bool.html) | Optional|An update of the app is required to parse this link|
|message|[string](/API_docs/types/string.html) | Yes|Message to show to the user|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [help.DeepLinkInfo](/API_docs/types/help.DeepLinkInfo.html)


### Example:

```
$help_deepLinkInfo = ['_' => 'help.deepLinkInfo', 'update_app' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  
