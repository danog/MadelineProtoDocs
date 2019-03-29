---
title: poll
description: Poll
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: poll  
[Back to constructors index](index.md)



Poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|closed|[Bool](../types/Bool.md) | Optional|Closed?|
|question|[string](../types/string.md) | Yes|Question|
|answers|Array of [PollAnswer](../types/PollAnswer.md) | Yes|Answers|



### Type: [Poll](../types/Poll.md)


### Example:

```php
$poll = ['_' => 'poll', 'id' => long, 'closed' => Bool, 'question' => 'string', 'answers' => [PollAnswer, PollAnswer]];
```  


Or, if you're into Lua:

```lua
poll={_='poll', id=long, closed=Bool, question='string', answers={PollAnswer}}

```


