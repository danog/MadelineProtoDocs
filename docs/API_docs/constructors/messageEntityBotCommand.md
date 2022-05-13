---
title: "messageEntityBotCommand"
description: "Message entity representing a bot /command"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBotCommand  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a bot /command

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityBotCommand = ['_' => 'messageEntityBotCommand', 'offset' => int, 'length' => int];
```  
