---
title: "inputBotInlineResultGame"
description: "Game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultGame  
[Back to constructors index](/API_docs/constructors/index.html)



Game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Result ID|
|short\_name|[string](/API_docs/types/string.html) | Yes|Game short name|
|send\_message|[InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](/API_docs/types/InputBotInlineResult.html)


### Example:

```
$inputBotInlineResultGame = ['_' => 'inputBotInlineResultGame', 'id' => 'string', 'short_name' => 'string', 'send_message' => InputBotInlineMessage];
```  
