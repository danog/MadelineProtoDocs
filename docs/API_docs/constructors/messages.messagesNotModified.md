---
title: "messages.messagesNotModified"
description: "No new messages matching the query were found"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messagesNotModified.html
---
# Constructor: messages.messagesNotModified  
[Back to constructors index](/API_docs/constructors/index.html)



No new messages matching the query were found

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of results found server-side by the given query|



### Type: [messages.Messages](/API_docs/types/messages.Messages.html)


### Example:

```
$messages_messagesNotModified = ['_' => 'messages.messagesNotModified', 'count' => int];
```  
