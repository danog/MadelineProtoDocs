---
title: "messageActionChatCreate"
description: "Group created"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatCreate  
[Back to constructors index](index.md)



Group created

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Group name|
|users|Array of [long](../types/long.md) | Yes|List of group members|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatCreate = ['_' => 'messageActionChatCreate', 'title' => 'string', 'users' => [long, long]];
```  
