---
title: "messageViews"
description: "View, forward counter + info about replies of a specific message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageViews  
[Back to constructors index](/API_docs/constructors/index.html)



View, forward counter + info about replies of a specific message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|[int](/API_docs/types/int.html) | Optional|View count of message|
|forwards|[int](/API_docs/types/int.html) | Optional|Forward count of message|
|replies|[MessageReplies](/API_docs/types/MessageReplies.html) | Optional|Reply and [thread](https://core.telegram.org/api/threads) information of message|



### Type: [MessageViews](/API_docs/types/MessageViews.html)


### Example:

```
$messageViews = ['_' => 'messageViews', 'views' => int, 'forwards' => int, 'replies' => MessageReplies];
```  
