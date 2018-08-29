---
title: answerInlineQuery
description: Bots only. Sets result of an inline query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: answerInlineQuery  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Bots only. Sets result of an inline query

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|inline\_query\_id|[int64](../constructors/int64.md) | Identifier of the inline query | Yes|
|is\_personal|[Bool](../types/Bool.md) | Does result of the query can be cached only for specified user | Yes|
|results|Array of [InputInlineQueryResult](../types/InputInlineQueryResult.md) | Results of the query | Yes|
|cache\_time|[int](../types/int.md) | Allowed time to cache results of the query in seconds | Yes|
|next\_offset|[string](../types/string.md) | Offset for the next inline query, pass empty string if there is no more results | Yes|
|switch\_pm\_text|[string](../types/string.md) | If non-empty, this text should be shown on the button, which opens private chat with the bot and sends bot start message with parameter switch_pm_parameter | Yes|
|switch\_pm\_parameter|[string](../types/string.md) | Parameter for the bot start message | Yes|


### Return type: [Ok](../types/Ok.md)

