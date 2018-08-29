---
title: setGameScore
description: Bots only. Updates game score of the specified user in the game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: setGameScore  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Bots only. Updates game score of the specified user in the game

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat a message with the game belongs to | Yes|
|message\_id|[int53](../types/int53.md) | Identifier of the message | Yes|
|edit\_message|[Bool](../types/Bool.md) | True, if message should be edited | Yes|
|user\_id|[int](../types/int.md) | User identifier | Yes|
|score|[int](../types/int.md) | New score | Yes|
|force|[Bool](../types/Bool.md) | Pass True to update the score even if it decreases. If score is 0, user will be deleted from the high scores table | Yes|


### Return type: [Message](../types/Message.md)

