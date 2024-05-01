---
title: "updateBotInlineSend"
description: "The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotInlineSend  
[Back to constructors index](/API_docs/constructors/index.html)



The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|The user that chose the result|
|query|[string](/API_docs/types/string.html) | Yes|The query that was used to obtain the result|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Optional. Sender location, only for bots that require user location|
|id|[string](/API_docs/types/string.html) | Yes|The unique identifier for the result that was chosen|
|msg\_id|[InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html) | Optional|Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotInlineSend = ['_' => 'updateBotInlineSend', 'user_id' => long, 'query' => 'string', 'geo' => GeoPoint, 'id' => 'string', 'msg_id' => InputBotInlineMessageID];
```  
