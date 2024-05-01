---
title: "updatesCombined"
description: "Constructor for a group of updates."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatesCombined  
[Back to constructors index](/API_docs/constructors/index.html)



Constructor for a group of updates.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|updates|Array of [Update](/API_docs/types/Update.html) | Yes|List of updates|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users mentioned in updates|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|List of chats mentioned in updates|
|date|[int](/API_docs/types/int.html) | Yes|Current date|
|seq\_start|[int](/API_docs/types/int.html) | Yes|Value **seq** for the earliest update in a group|
|seq|[int](/API_docs/types/int.html) | Yes|Value **seq** for the latest update in a group|



### Type: [Updates](/API_docs/types/Updates.html)


### Example:

```
$updatesCombined = ['_' => 'updatesCombined', 'updates' => [Update, Update], 'users' => [User, User], 'chats' => [Chat, Chat], 'date' => int, 'seq_start' => int, 'seq' => int];
```  
