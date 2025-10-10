---
title: "updatePaidReactionPrivacy"
description: "Contains the current default paid reaction privacy, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePaidReactionPrivacy  
[Back to constructors index](/API_docs/constructors/index.html)



Contains the current [default paid reaction privacy, see here »](https://core.telegram.org/api/reactions#paid-reactions) for more info.

Clients should invoke [messages.getPaidReactionPrivacy](../methods/messages.getPaidReactionPrivacy.html) on startup to fetch the current default reaction privacy because this update is only sent to currently online sessions and cannot be fetched using getDifference on client startup.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|private|[PaidReactionPrivacy](/API_docs/types/PaidReactionPrivacy.html) | Yes|Paid reaction privacy settings.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePaidReactionPrivacy = ['_' => 'updatePaidReactionPrivacy', 'private' => PaidReactionPrivacy];
```  
