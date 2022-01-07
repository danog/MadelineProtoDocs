---
title: "messageUserReaction"
description: "Message reaction"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserReaction  
[Back to constructors index](index.md)



Message reaction

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|reaction|[string](../types/string.md) | Yes|Reaction (UTF8 emoji)|



### Type: [MessageUserReaction](../types/MessageUserReaction.md)


### Example:

```php
$messageUserReaction = ['_' => 'messageUserReaction', 'user_id' => long, 'reaction' => 'string'];
```  
