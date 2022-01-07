---
title: "updateGroupCallParticipants"
description: "updateGroupCallParticipants attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallParticipants  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.md) | Yes|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md) | Yes|
|version|[int](/API_docs/types/int.md) | Yes|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateGroupCallParticipants = ['_' => 'updateGroupCallParticipants', 'call' => InputGroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'version' => int];
```  
