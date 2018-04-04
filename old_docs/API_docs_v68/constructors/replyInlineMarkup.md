---
title: replyInlineMarkup
description: replyInlineMarkup attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: replyInlineMarkup  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|rows|Array of [KeyboardButtonRow](../types/KeyboardButtonRow.md) | Yes|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```
$replyInlineMarkup = ['_' => 'replyInlineMarkup', 'rows' => [KeyboardButtonRow, KeyboardButtonRow]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "replyInlineMarkup", "rows": [KeyboardButtonRow]}
```


Or, if you're into Lua:  


```
replyInlineMarkup={_='replyInlineMarkup', rows={KeyboardButtonRow}}

```


