---
title: "updateGroupCallParticipants"
description: "updateGroupCallParticipants attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|
|version|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateGroupCallParticipants = ['_' => 'updateGroupCallParticipants', 'call' => InputGroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'version' => int];
```  
