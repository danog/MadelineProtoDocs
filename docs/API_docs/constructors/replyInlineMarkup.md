---
title: "replyInlineMarkup"
description: "Bot or inline keyboard"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyInlineMarkup  
[Back to constructors index](/API_docs/constructors/index.html)



Bot or inline keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|force\_reply|[Bool](/API_docs/types/Bool.html) | Optional|
|rows|Array of [KeyboardInlineButtonRow](/API_docs/types/KeyboardInlineButtonRow.html) | Yes|Bot or inline keyboard rows|



### Type: [ReplyMarkup](/API_docs/types/ReplyMarkup.html)


### Example:

```
$replyInlineMarkup = ['_' => 'replyInlineMarkup', 'force_reply' => Bool, 'rows' => [KeyboardInlineButtonRow, KeyboardInlineButtonRow]];
```  
