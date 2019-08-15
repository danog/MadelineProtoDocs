---
title: updateMessagePoll
description: Update message poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePoll  
[Back to constructors index](index.md)



Update message poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll\_id|[long](../types/long.md) | Yes|Poll ID|
|poll|[Poll](../types/Poll.md) | Optional|Poll|
|results|[PollResults](../types/PollResults.md) | Yes|Results|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateMessagePoll = ['_' => 'updateMessagePoll', 'poll_id' => long, 'poll' => Poll, 'results' => PollResults];
```  


Or, if you're into Lua:

```lua
updateMessagePoll={_='updateMessagePoll', poll_id=long, poll=Poll, results=PollResults}

```


