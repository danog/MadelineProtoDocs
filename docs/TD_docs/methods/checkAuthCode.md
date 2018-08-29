---
title: checkAuthCode
description: Checks authentication code. Works only when getAuthState returns authStateWaitCode. Returns authStateWaitPassword or authStateOk on success
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: checkAuthCode  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Checks authentication code. Works only when getAuthState returns authStateWaitCode. Returns authStateWaitPassword or authStateOk on success

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](../types/string.md) | Verification code from SMS, Telegram message, phone call or flash call | Yes|
|first\_name|[string](../types/string.md) | User first name, if user is yet not registered, 1-255 characters | Yes|
|last\_name|[string](../types/string.md) | Optional user last name, if user is yet not registered, 0-255 characters | Yes|


### Return type: [AuthState](../types/AuthState.md)

