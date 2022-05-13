---
title: "messageUserVoteMultiple"
description: "How a user voted in a multiple-choice poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVoteMultiple  
[Back to constructors index](/API_docs/constructors/index.html)



How a user voted in a multiple-choice poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|options|Array of [bytes](/API_docs/types/bytes.html) | Yes|Options chosen by the user|
|date|[int](/API_docs/types/int.html) | Yes|When did the user cast their votes|



### Type: [MessageUserVote](/API_docs/types/MessageUserVote.html)


### Example:

```
$messageUserVoteMultiple = ['_' => 'messageUserVoteMultiple', 'user_id' => long, 'options' => ['bytes', 'bytes'], 'date' => int];
```  
