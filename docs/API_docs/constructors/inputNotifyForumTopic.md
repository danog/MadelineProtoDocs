---
title: "inputNotifyForumTopic"
description: "inputNotifyForumTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputNotifyForumTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [InputNotifyPeer](/API_docs/types/InputNotifyPeer.html)


### Example:

```
$inputNotifyForumTopic = ['_' => 'inputNotifyForumTopic', 'peer' => InputPeer, 'top_msg_id' => int];
```  
