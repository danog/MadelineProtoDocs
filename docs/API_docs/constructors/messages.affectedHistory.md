---
title: "messages.affectedHistory"
description: "Affected part of communication history with the user or in a chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_affectedHistory.html
---
# Constructor: messages.affectedHistory  
[Back to constructors index](/API_docs/constructors/index.html)



Affected part of communication history with the user or in a chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](/API_docs/types/int.html) | Yes|Number of events occurred in a text box|
|pts\_count|[int](/API_docs/types/int.html) | Yes|Number of affected events|
|offset|[int](/API_docs/types/int.html) | Yes|If a parameter contains positive value, it is necessary to repeat the method call using the given value; during the proceeding of all the history the value itself shall gradually decrease|



### Type: [messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)


### Example:

```
$messages_affectedHistory = ['_' => 'messages.affectedHistory', 'pts' => int, 'pts_count' => int, 'offset' => int];
```  
