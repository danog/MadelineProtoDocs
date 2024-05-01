---
title: "updateMessagePoll"
description: "The results of a poll have changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePoll  
[Back to constructors index](/API_docs/constructors/index.html)



The results of a poll have changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll\_id|[long](/API_docs/types/long.html) | Yes|Poll ID|
|poll|[Poll](/API_docs/types/Poll.html) | Optional|If the server knows the client hasn't cached this poll yet, the poll itself|
|results|[PollResults](/API_docs/types/PollResults.html) | Yes|New poll results|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessagePoll = ['_' => 'updateMessagePoll', 'poll_id' => long, 'poll' => Poll, 'results' => PollResults];
```  
