---
title: changePhoneNumber
description: Changes user's phone number and sends authentication code to the new user's phone number. Returns authStateWaitCode with information about sent code on success
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: changePhoneNumber  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Changes user's phone number and sends authentication code to the new user's phone number. Returns authStateWaitCode with information about sent code on success

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | New user's phone number in any reasonable format | Yes|
|allow\_flash\_call|[Bool](../types/Bool.md) | Pass True, if code can be sent via flash call to the specified phone number | Yes|
|is\_current\_phone\_number|[Bool](../types/Bool.md) | Pass true, if the phone number is used on the current device. Ignored if allow_flash_call is False | Yes|


### Return type: [AuthState](../types/AuthState.md)

