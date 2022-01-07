---
title: "replyInlineMarkup"
description: "Bot or inline keyboard"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyInlineMarkup  
[Back to constructors index](/API_docs/constructors/index.md)



Bot or inline keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|rows|Array of [KeyboardButtonRow](/API_docs/types/KeyboardButtonRow.md) | Yes|Bot or inline keyboard rows|



### Type: [ReplyMarkup](/API_docs/types/ReplyMarkup.md)


### Example:

```php
$replyInlineMarkup = ['_' => 'replyInlineMarkup', 'rows' => [KeyboardButtonRow, KeyboardButtonRow]];
```  
