---
title: "messageUserVoteMultiple"
description: "How a user voted in a multiple-choice poll"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageUserVoteMultiple  
[Back to constructors index](/API_docs/constructors/index.md)



How a user voted in a multiple-choice poll

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|options|Array of [bytes](/API_docs/types/bytes.md) | Yes|Options chosen by the user|
|date|[int](/API_docs/types/int.md) | Yes|When did the user cast their votes|



### Type: [MessageUserVote](/API_docs/types/MessageUserVote.md)


### Example:

```php
$messageUserVoteMultiple = ['_' => 'messageUserVoteMultiple', 'user_id' => long, 'options' => ['bytes', 'bytes'], 'date' => int];
```  
