---
title: "messageActionNoForwardsRequest"
description: "messageActionNoForwardsRequest attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionNoForwardsRequest  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expired|[Bool](/API_docs/types/Bool.html) | Optional|
|prev\_value|[Bool](/API_docs/types/Bool.html) | Yes|
|new\_value|[Bool](/API_docs/types/Bool.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionNoForwardsRequest = ['_' => 'messageActionNoForwardsRequest', 'expired' => Bool, 'prev_value' => Bool, 'new_value' => Bool];
```  
