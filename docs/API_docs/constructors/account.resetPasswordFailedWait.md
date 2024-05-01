---
title: "account.resetPasswordFailedWait"
description: "You recently requested a password reset that was canceled, please wait until the specified date before requesting another reset."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_resetPasswordFailedWait.html
---
# Constructor: account.resetPasswordFailedWait  
[Back to constructors index](/API_docs/constructors/index.html)



You recently requested a password reset that was canceled, please wait until the specified date before requesting another reset.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|retry\_date|[int](/API_docs/types/int.html) | Yes|Wait until this date before requesting another reset.|



### Type: [account.ResetPasswordResult](/API_docs/types/account.ResetPasswordResult.html)


### Example:

```
$account_resetPasswordFailedWait = ['_' => 'account.resetPasswordFailedWait', 'retry_date' => int];
```  
