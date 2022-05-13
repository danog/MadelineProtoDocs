---
title: "messageUserVote"
description: "How a user voted in a poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVote  
[Back to constructors index](/API_docs/constructors/index.html)



How a user voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|option|[bytes](/API_docs/types/bytes.html) | Yes|The option chosen by the user|
|date|[int](/API_docs/types/int.html) | Yes|When did the user cast the vote|



### Type: [MessageUserVote](/API_docs/types/MessageUserVote.html)


### Example:

```
$messageUserVote = ['_' => 'messageUserVote', 'user_id' => long, 'option' => 'bytes', 'date' => int];
```  
