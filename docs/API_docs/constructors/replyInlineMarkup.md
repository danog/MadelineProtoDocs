---
title: "replyInlineMarkup"
description: "Bot or inline keyboard"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyInlineMarkup  
[Back to constructors index](index.md)



Bot or inline keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|rows|Array of [KeyboardButtonRow](../types/KeyboardButtonRow.md) | Yes|Bot or inline keyboard rows|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyInlineMarkup = ['_' => 'replyInlineMarkup', 'rows' => [KeyboardButtonRow, KeyboardButtonRow]];
```  
