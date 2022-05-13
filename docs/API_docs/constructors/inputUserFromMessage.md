---
title: "inputUserFromMessage"
description: "Defines a min user that was seen in a certain message of a certain chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUserFromMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a [min](https://core.telegram.org/api/min) user that was seen in a certain message of a certain chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|The chat where the user was seen|
|msg\_id|[int](/API_docs/types/int.html) | Yes|The message ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|The identifier of the user that was seen|



### Type: [InputUser](/API_docs/types/InputUser.html)


### Example:

```
$inputUserFromMessage = ['_' => 'inputUserFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'user_id' => long];
```  
