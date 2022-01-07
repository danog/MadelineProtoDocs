---
title: "help.deepLinkInfo"
description: "Deep linking info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_deepLinkInfo.html
---
# Constructor: help.deepLinkInfo  
[Back to constructors index](index.md)



Deep linking info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update\_app|[Bool](../types/Bool.md) | Optional|An update of the app is required to parse this link|
|message|[string](../types/string.md) | Yes|Message to show to the user|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [help.DeepLinkInfo](../types/help.DeepLinkInfo.md)


### Example:

```php
$help_deepLinkInfo = ['_' => 'help.deepLinkInfo', 'update_app' => Bool, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  
