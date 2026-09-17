---
title: "sendMessageRichMessageDraftAction"
description: "sendMessageRichMessageDraftAction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendMessageRichMessageDraftAction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|can\_stop|[Bool](/API_docs/types/Bool.html) | Optional|
|keep\_on\_stop|[Bool](/API_docs/types/Bool.html) | Optional|
|rich\_message|[RichMessage](/API_docs/types/RichMessage.html) | Yes|



### Type: [SendMessageAction](/API_docs/types/SendMessageAction.html)


### Example:

```
$sendMessageRichMessageDraftAction = ['_' => 'sendMessageRichMessageDraftAction', 'can_stop' => Bool, 'keep_on_stop' => Bool, 'rich_message' => RichMessage];
```  
