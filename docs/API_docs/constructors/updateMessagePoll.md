---
title: "updateMessagePoll"
description: "The results of a poll have changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePoll  
[Back to constructors index](index.md)



The results of a poll have changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll\_id|[long](../types/long.md) | Yes|Poll ID|
|poll|[Poll](../types/Poll.md) | Optional|If the server knows the client hasn't cached this poll yet, the poll itself|
|results|[PollResults](../types/PollResults.md) | Yes|New poll results|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateMessagePoll = ['_' => 'updateMessagePoll', 'poll_id' => long, 'poll' => Poll, 'results' => PollResults];
```  


Or, if you're into Lua:

```lua
updateMessagePoll={_='updateMessagePoll', poll_id=long, poll=Poll, results=PollResults}

```


