---
title: recoverAuthPassword
description: Recovers password with recovery code sent to email. Works only when getAuthState returns authStateWaitPassword. Returns authStateOk on success
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: recoverAuthPassword  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Recovers password with recovery code sent to email. Works only when getAuthState returns authStateWaitPassword. Returns authStateOk on success

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|recovery\_code|[string](../types/string.md) | Recovery code to check | Yes|


### Return type: [AuthState](../types/AuthState.md)

