---
title: setAuthPhoneNumber
description: Sets user's phone number and sends authentication code to the user. Works only when getAuthState returns authStateWaitPhoneNumber. If phone number is not recognized or another error has happened, returns an error. Otherwise returns authStateWaitCode
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: setAuthPhoneNumber  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Sets user's phone number and sends authentication code to the user. Works only when getAuthState returns authStateWaitPhoneNumber. If phone number is not recognized or another error has happened, returns an error. Otherwise returns authStateWaitCode

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | User's phone number in any reasonable format | Yes|
|allow\_flash\_call|[Bool](../types/Bool.md) | Pass True, if code can be sent via flash call to the specified phone number | Yes|
|is\_current\_phone\_number|[Bool](../types/Bool.md) | Pass true, if the phone number is used on the current device. Ignored if allow_flash_call is False | Yes|


### Return type: [AuthState](../types/AuthState.md)

