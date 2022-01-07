---
title: "replyKeyboardHide"
description: "Hide sent bot keyboard"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardHide  
[Back to constructors index](index.md)



Hide sent bot keyboard

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|selective|[Bool](../types/Bool.md) | Optional|Use this flag if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply\_to\_message\_id), sender of the original message.<br><br>Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet|



### Type: [ReplyMarkup](../types/ReplyMarkup.md)


### Example:

```php
$replyKeyboardHide = ['_' => 'replyKeyboardHide', 'selective' => Bool];
```  
