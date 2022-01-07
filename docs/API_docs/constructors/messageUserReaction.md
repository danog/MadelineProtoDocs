---
title: "messageUserReaction"
description: "Message reaction"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserReaction  
[Back to constructors index](/API_docs/constructors/index.html)



Message reaction

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|reaction|[string](/API_docs/types/string.html) | Yes|Reaction (UTF8 emoji)|



### Type: [MessageUserReaction](/API_docs/types/MessageUserReaction.html)


### Example:

```php
$messageUserReaction = ['_' => 'messageUserReaction', 'user_id' => long, 'reaction' => 'string'];
```  
