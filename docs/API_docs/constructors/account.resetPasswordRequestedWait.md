---
title: "account.resetPasswordRequestedWait"
description: "You successfully requested a password reset, please wait until the specified date before finalizing the reset."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_resetPasswordRequestedWait.html
---
# Constructor: account.resetPasswordRequestedWait  
[Back to constructors index](/API_docs/constructors/index.html)



You successfully requested a password reset, please wait until the specified date before finalizing the reset.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|until\_date|[int](/API_docs/types/int.html) | Yes|Wait until this date before finalizing the reset.|



### Type: [account.ResetPasswordResult](/API_docs/types/account.ResetPasswordResult.html)


### Example:

```
$account_resetPasswordRequestedWait = ['_' => 'account.resetPasswordRequestedWait', 'until_date' => int];
```  
