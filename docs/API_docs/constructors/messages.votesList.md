---
title: "messages.votesList"
description: "How users voted in a poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_votesList.html
---
# Constructor: messages.votesList  
[Back to constructors index](/API_docs/constructors/index.md)



How users voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.md) | Yes|Total number of votes for all options (or only for the chosen `option`, if provided to [messages.getPollVotes](../methods/messages.getPollVotes.md))|
|votes|Array of [MessageUserVote](/API_docs/types/MessageUserVote.md) | Yes|Vote info for each user|
|users|Array of [User](/API_docs/types/User.md) | Yes|Info about users that voted in the poll|
|next\_offset|[string](/API_docs/types/string.md) | Optional|Offset to use with the next [messages.getPollVotes](../methods/messages.getPollVotes.md) request, empty string if no more results are available.|



### Type: [messages.VotesList](/API_docs/types/messages.VotesList.md)


### Example:

```php
$messages_votesList = ['_' => 'messages.votesList', 'count' => int, 'votes' => [MessageUserVote, MessageUserVote], 'users' => [User, User], 'next_offset' => 'string'];
```  
