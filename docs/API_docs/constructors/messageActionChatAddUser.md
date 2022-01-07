---
title: "messageActionChatAddUser"
description: "New member in the group"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatAddUser  
[Back to constructors index](/API_docs/constructors/index.md)



New member in the group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](/API_docs/types/long.md) | Yes|Users that were invited to the chat|



### Type: [MessageAction](/API_docs/types/MessageAction.md)


### Example:

```php
$messageActionChatAddUser = ['_' => 'messageActionChatAddUser', 'users' => [long, long]];
```  
