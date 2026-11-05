---
title: "messageMediaWidget"
description: "messageMediaWidget attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaWidget  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|is\_copy|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_query|[Bool](/API_docs/types/Bool.html) | Optional|
|background\_query|[Bool](/API_docs/types/Bool.html) | Optional|
|width|[int](/API_docs/types/int.html) | Yes|
|height|[int](/API_docs/types/int.html) | Yes|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|
|public\_data|[string](/API_docs/types/string.html) | Optional|
|public\_data\_hash|[long](/API_docs/types/long.html) | Optional|
|chat\_data|[string](/API_docs/types/string.html) | Optional|
|widget\_id|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaWidget = ['_' => 'messageMediaWidget', 'is_copy' => Bool, 'can_query' => Bool, 'background_query' => Bool, 'width' => int, 'height' => int, 'payload' => 'bytes', 'public_data' => 'string', 'public_data_hash' => long, 'chat_data' => 'string', 'widget_id' => long];
```  
