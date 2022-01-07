---
title: "messageActionChatMigrateTo"
description: "Indicates the chat was migrated to the specified supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatMigrateTo  
[Back to constructors index](/API_docs/constructors/index.md)



Indicates the chat was [migrated](https://core.telegram.org/api/channel) to the specified supergroup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.md) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.md)


### Example:

```php
$messageActionChatMigrateTo = ['_' => 'messageActionChatMigrateTo', 'channel_id' => long];
```  
