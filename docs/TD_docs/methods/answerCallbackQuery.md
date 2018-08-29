---
title: answerCallbackQuery
description: Bots only. Sets result of a callback query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: answerCallbackQuery  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Bots only. Sets result of a callback query

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|callback\_query\_id|[int64](../constructors/int64.md) | Identifier of the callback query | Yes|
|text|[string](../types/string.md) | Text of the answer | Yes|
|show\_alert|[Bool](../types/Bool.md) | If true, an alert should be shown to the user instead of a toast | Yes|
|url|[string](../types/string.md) | Url to be opened | Yes|
|cache\_time|[int](../types/int.md) | Allowed time to cache result of the query in seconds | Yes|


### Return type: [Ok](../types/Ok.md)

