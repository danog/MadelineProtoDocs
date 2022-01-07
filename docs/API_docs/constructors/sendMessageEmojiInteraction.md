---
title: "sendMessageEmojiInteraction"
description: "sendMessageEmojiInteraction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageEmojiInteraction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|emoticon|[string](/API_docs/types/string.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|interaction|[DataJSON](/API_docs/types/DataJSON.html) | Yes|



### Type: [SendMessageAction](/API_docs/types/SendMessageAction.html)


### Example:

```php
$sendMessageEmojiInteraction = ['_' => 'sendMessageEmojiInteraction', 'emoticon' => 'string', 'msg_id' => int, 'interaction' => DataJSON];
```  
