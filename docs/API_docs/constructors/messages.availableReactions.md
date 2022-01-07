---
title: "messages.availableReactions"
description: "messages.availableReactions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_availableReactions.html
---
# Constructor: messages.availableReactions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](/API_docs/types/int.html) | Yes|
|reactions|Array of [AvailableReaction](/API_docs/types/AvailableReaction.html) | Yes|



### Type: [messages.AvailableReactions](/API_docs/types/messages.AvailableReactions.html)


### Example:

```php
$messages_availableReactions = ['_' => 'messages.availableReactions', 'hash' => int, 'reactions' => [AvailableReaction, AvailableReaction]];
```  
