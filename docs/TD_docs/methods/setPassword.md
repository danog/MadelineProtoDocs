---
title: setPassword
description: Changes user password. If new recovery email is specified, then error EMAIL_UNCONFIRMED is returned and password change will not be applied until email confirmation. Application should call getPasswordState from time to time to check if email is already confirmed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: setPassword  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Changes user password. If new recovery email is specified, then error EMAIL_UNCONFIRMED is returned and password change will not be applied until email confirmation. Application should call getPasswordState from time to time to check if email is already confirmed

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|old\_password|[string](../types/string.md) | Old user password | Yes|
|new\_password|[string](../types/string.md) | New user password, may be empty to remove the password | Yes|
|new\_hint|[string](../types/string.md) | New password hint, can be empty | Yes|
|set\_recovery\_email|[Bool](../types/Bool.md) | Pass True, if recovery email should be changed | Yes|
|new\_recovery\_email|[string](../types/string.md) | New recovery email, may be empty | Yes|


### Return type: [PasswordState](../types/PasswordState.md)

