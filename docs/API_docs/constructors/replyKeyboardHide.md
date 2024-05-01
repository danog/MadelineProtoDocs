---
title: "replyKeyboardHide"
description: "Hide sent bot keyboard"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardHide  
[Back to constructors index](/API_docs/constructors/index.html)



Hide sent bot keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|selective|[Bool](/API_docs/types/Bool.html) | Optional|Use this flag if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply\_to\_message\_id), sender of the original message.<br><br>Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet|



### Type: [ReplyMarkup](/API_docs/types/ReplyMarkup.html)


### Example:

```
$replyKeyboardHide = ['_' => 'replyKeyboardHide', 'selective' => Bool];
```  
