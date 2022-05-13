---
title: "replyKeyboardForceReply"
description: "Force the user to send a reply"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: replyKeyboardForceReply  
[Back to constructors index](/API_docs/constructors/index.html)



Force the user to send a reply

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|single\_use|[Bool](/API_docs/types/Bool.html) | Optional|Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again.|
|selective|[Bool](/API_docs/types/Bool.html) | Optional|Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply\_to\_message\_id), sender of the original message. <br>Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.|
|placeholder|[string](/API_docs/types/string.html) | Optional|The placeholder to be shown in the input field when the keyboard is active; 1-64 characters.|



### Type: [ReplyMarkup](/API_docs/types/ReplyMarkup.html)


### Example:

```
$replyKeyboardForceReply = ['_' => 'replyKeyboardForceReply', 'single_use' => Bool, 'selective' => Bool, 'placeholder' => 'string'];
```  
