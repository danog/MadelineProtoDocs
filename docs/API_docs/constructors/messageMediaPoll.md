---
title: "messageMediaPoll"
description: "Poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPoll  
[Back to constructors index](/API_docs/constructors/index.html)



Poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll|[Poll](/API_docs/types/Poll.html) | Yes|The poll|
|results|[PollResults](/API_docs/types/PollResults.html) | Yes|The results of the poll|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaPoll = ['_' => 'messageMediaPoll', 'poll' => Poll, 'results' => PollResults];
```  
