---
title: messageMediaPoll
description: Message media poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPoll  
[Back to constructors index](index.md)



Message media poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](../types/Poll.md) | Yes|Poll|
|results|[PollResults](../types/PollResults.md) | Yes|Results|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaPoll = ['_' => 'messageMediaPoll', 'poll' => Poll, 'results' => PollResults];
```  


Or, if you're into Lua:

```lua
messageMediaPoll={_='messageMediaPoll', poll=Poll, results=PollResults}

```


