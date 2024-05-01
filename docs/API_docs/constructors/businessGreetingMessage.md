---
title: "businessGreetingMessage"
description: "businessGreetingMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessGreetingMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|
|recipients|[BusinessRecipients](/API_docs/types/BusinessRecipients.html) | Yes|
|no\_activity\_days|[int](/API_docs/types/int.html) | Yes|



### Type: [BusinessGreetingMessage](/API_docs/types/BusinessGreetingMessage.html)


### Example:

```
$businessGreetingMessage = ['_' => 'businessGreetingMessage', 'shortcut_id' => int, 'recipients' => BusinessRecipients, 'no_activity_days' => int];
```  
