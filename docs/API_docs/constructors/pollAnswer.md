---
title: "pollAnswer"
description: "A possible answer of a poll"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pollAnswer  
[Back to constructors index](index.md)



A possible answer of a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Textual representation of the answer|
|option|[bytes](../types/bytes.md) | Yes|The param that has to be passed to [messages.sendVote](../methods/messages.sendVote.md).|



### Type: [PollAnswer](../types/PollAnswer.md)


### Example:

```php
$pollAnswer = ['_' => 'pollAnswer', 'text' => 'string', 'option' => 'bytes'];
```  


Or, if you're into Lua:

```lua
pollAnswer={_='pollAnswer', text='string', option='bytes'}

```


