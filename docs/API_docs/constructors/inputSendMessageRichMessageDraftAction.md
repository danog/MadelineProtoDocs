---
title: "inputSendMessageRichMessageDraftAction"
description: "inputSendMessageRichMessageDraftAction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSendMessageRichMessageDraftAction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|can\_stop|[Bool](/API_docs/types/Bool.html) | Optional|
|keep\_on\_stop|[Bool](/API_docs/types/Bool.html) | Optional|
|rich\_message|[InputRichMessage](/API_docs/types/InputRichMessage.html) | Yes|



### Type: [SendMessageAction](/API_docs/types/SendMessageAction.html)


### Example:

```
$inputSendMessageRichMessageDraftAction = ['_' => 'inputSendMessageRichMessageDraftAction', 'can_stop' => Bool, 'keep_on_stop' => Bool, 'rich_message' => InputRichMessage];
```  
