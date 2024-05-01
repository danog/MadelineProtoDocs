---
title: "inputMessageCallbackQuery"
description: "Used by bots for fetching information about the message that originated a callback query"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageCallbackQuery  
[Back to constructors index](/API_docs/constructors/index.html)



Used by bots for fetching information about the message that originated a callback query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|Message ID|
|query\_id|[long](/API_docs/types/long.html) | Yes|Callback query ID|



### Type: [InputMessage](/API_docs/types/InputMessage.html)


### Example:

```
$inputMessageCallbackQuery = ['_' => 'inputMessageCallbackQuery', 'id' => int, 'query_id' => long];
```  
