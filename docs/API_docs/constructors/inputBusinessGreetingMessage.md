---
title: "inputBusinessGreetingMessage"
description: "inputBusinessGreetingMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessGreetingMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|
|recipients|[InputBusinessRecipients](/API_docs/types/InputBusinessRecipients.html) | Yes|
|no\_activity\_days|[int](/API_docs/types/int.html) | Yes|



### Type: [InputBusinessGreetingMessage](/API_docs/types/InputBusinessGreetingMessage.html)


### Example:

```
$inputBusinessGreetingMessage = ['_' => 'inputBusinessGreetingMessage', 'shortcut_id' => int, 'recipients' => InputBusinessRecipients, 'no_activity_days' => int];
```  
