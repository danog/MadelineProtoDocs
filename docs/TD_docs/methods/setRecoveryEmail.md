---
title: setRecoveryEmail
description: Changes user recovery email. If new recovery email is specified, then error EMAIL_UNCONFIRMED is returned and email will not be changed until email confirmation. Application should call getPasswordState from time to time to check if email is already confirmed. -If new_recovery_email coincides with the current set up email succeeds immediately and aborts all other requests waiting for email confirmation
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: setRecoveryEmail  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Changes user recovery email. If new recovery email is specified, then error EMAIL_UNCONFIRMED is returned and email will not be changed until email confirmation. Application should call getPasswordState from time to time to check if email is already confirmed. -If new_recovery_email coincides with the current set up email succeeds immediately and aborts all other requests waiting for email confirmation

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[string](../types/string.md) | Current user password | Yes|
|new\_recovery\_email|[string](../types/string.md) | New recovery email | Yes|


### Return type: [PasswordState](../types/PasswordState.md)

