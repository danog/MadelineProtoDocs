---
title: messages.votesList
description: messages.votesList attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_votesList.html
---
# Constructor: messages.votesList  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|votes|Array of [MessageUserVote](../types/MessageUserVote.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|next\_offset|[string](../types/string.md) | Optional|



### Type: [messages.VotesList](../types/messages.VotesList.md)


### Example:

```php
$messages.votesList = ['_' => 'messages.votesList', 'count' => int, 'votes' => [MessageUserVote, MessageUserVote], 'users' => [User, User], 'next_offset' => 'string'];
```  


Or, if you're into Lua:

```lua
messages.votesList={_='messages.votesList', count=int, votes={MessageUserVote}, users={User}, next_offset='string'}

```


