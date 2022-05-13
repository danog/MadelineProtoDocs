---
title: "messages.botResults"
description: "Result of a query to an inline bot"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_botResults.html
---
# Constructor: messages.botResults  
[Back to constructors index](/API_docs/constructors/index.html)



Result of a query to an inline bot

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|gallery|[Bool](/API_docs/types/Bool.html) | Optional|Whether the result is a picture gallery|
|query\_id|[long](/API_docs/types/long.html) | Yes|Query ID|
|next\_offset|[string](/API_docs/types/string.html) | Optional|The next offset to use when navigating through results|
|switch\_pm|[InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.html) | Optional|Whether the bot requested the user to message them in private|
|results|Array of [BotInlineResult](/API_docs/types/BotInlineResult.html) | Yes|The results|
|cache\_time|[int](/API_docs/types/int.html) | Yes|Caching validity of the results|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the results|



### Type: [messages.BotResults](/API_docs/types/messages.BotResults.html)


### Example:

```
$messages_botResults = ['_' => 'messages.botResults', 'gallery' => Bool, 'query_id' => long, 'next_offset' => 'string', 'switch_pm' => InlineBotSwitchPM, 'results' => [BotInlineResult, BotInlineResult], 'cache_time' => int, 'users' => [User, User]];
```  
