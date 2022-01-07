---
title: "messageUserVoteInputOption"
description: "How a user voted in a poll (reduced constructor, returned if an option was provided to messages.getPollVotes)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVoteInputOption  
[Back to constructors index](/API_docs/constructors/index.md)



How a user voted in a poll (reduced constructor, returned if an `option` was provided to [messages.getPollVotes](../methods/messages.getPollVotes.md))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|When did the user cast the vote|



### Type: [MessageUserVote](/API_docs/types/MessageUserVote.md)


### Example:

```php
$messageUserVoteInputOption = ['_' => 'messageUserVoteInputOption', 'user_id' => long, 'date' => int];
```  
