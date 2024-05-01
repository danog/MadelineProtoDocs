---
title: "messageActionSetMessagesTTL"
description: "The Time-To-Live of messages in this chat was changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSetMessagesTTL  
[Back to constructors index](/API_docs/constructors/index.html)



The Time-To-Live of messages in this chat was changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|period|[int](/API_docs/types/int.html) | Yes|New Time-To-Live of all messages sent in this chat; if 0, autodeletion was disabled.|
|auto\_setting\_from|[long](/API_docs/types/long.html) | Optional|If set, the chat TTL setting was set not due to a manual change by one of participants, but automatically because one of the participants has the [default TTL settings enabled »](../methods/messages.setDefaultHistoryTTL.html). For example, when a user writes to us for the first time and we have set a default messages TTL of 1 week, this service message (with `auto_setting_from=our_userid`) will be emitted before our first message.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSetMessagesTTL = ['_' => 'messageActionSetMessagesTTL', 'period' => int, 'auto_setting_from' => long];
```  
