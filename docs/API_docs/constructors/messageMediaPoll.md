---
title: "messageMediaPoll"
description: "Poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPoll  
[Back to constructors index](index.md)



Poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](../types/Poll.md) | Yes|The poll|
|results|[PollResults](../types/PollResults.md) | Yes|The results of the poll|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaPoll = ['_' => 'messageMediaPoll', 'poll' => Poll, 'results' => PollResults];
```  
