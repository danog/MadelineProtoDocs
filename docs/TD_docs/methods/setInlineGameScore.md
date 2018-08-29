---
title: setInlineGameScore
description: Bots only. Updates game score of the specified user in the game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: setInlineGameScore  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Bots only. Updates game score of the specified user in the game

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|inline\_message\_id|[string](../types/string.md) | Inline message identifier | Yes|
|edit\_message|[Bool](../types/Bool.md) | True, if message should be edited | Yes|
|user\_id|[int](../types/int.md) | User identifier | Yes|
|score|[int](../types/int.md) | New score | Yes|
|force|[Bool](../types/Bool.md) | Pass True to update the score even if it decreases. If score is 0, user will be deleted from the high scores table | Yes|


### Return type: [Ok](../types/Ok.md)

