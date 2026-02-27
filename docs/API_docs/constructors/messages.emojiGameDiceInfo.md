---
title: "messages.emojiGameDiceInfo"
description: "messages.emojiGameDiceInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_emojiGameDiceInfo.html
---
# Constructor: messages.emojiGameDiceInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|game\_hash|[string](/API_docs/types/string.html) | Yes|
|prev\_stake|[long](/API_docs/types/long.html) | Yes|
|current\_streak|[int](/API_docs/types/int.html) | Yes|
|params|Array of [int](/API_docs/types/int.html) | Yes|
|plays\_left|[int](/API_docs/types/int.html) | Optional|



### Type: [messages.EmojiGameInfo](/API_docs/types/messages.EmojiGameInfo.html)


### Example:

```
$messages_emojiGameDiceInfo = ['_' => 'messages.emojiGameDiceInfo', 'game_hash' => 'string', 'prev_stake' => long, 'current_streak' => int, 'params' => [int, int], 'plays_left' => int];
```  
