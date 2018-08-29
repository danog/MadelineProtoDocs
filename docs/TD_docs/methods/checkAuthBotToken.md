---
title: checkAuthBotToken
description: Check bot's authentication token to log in as a bot. Works only when getAuthState returns authStateWaitPhoneNumber. Can be used instead of setAuthPhoneNumber and checkAuthCode to log in. Returns authStateOk on success
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: checkAuthBotToken  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Check bot's authentication token to log in as a bot. Works only when getAuthState returns authStateWaitPhoneNumber. Can be used instead of setAuthPhoneNumber and checkAuthCode to log in. Returns authStateOk on success

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[string](../types/string.md) | Bot token | Yes|


### Return type: [AuthState](../types/AuthState.md)

