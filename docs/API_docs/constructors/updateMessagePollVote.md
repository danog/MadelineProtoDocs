---
title: "updateMessagePollVote"
description: "A specific user has voted in a poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessagePollVote  
[Back to constructors index](/API_docs/constructors/index.html)



A specific user has voted in a poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|poll\_id|[long](/API_docs/types/long.html) | Yes|Poll ID|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|options|Array of [bytes](/API_docs/types/bytes.html) | Yes|Chosen option(s)|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateMessagePollVote = ['_' => 'updateMessagePollVote', 'poll_id' => long, 'user_id' => long, 'options' => ['bytes', 'bytes'], 'qts' => int];
```  
