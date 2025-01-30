---
title: "inputPrivacyKeyStatusTimestamp"
description: "Whether people will be able to see our exact last online timestamp."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyKeyStatusTimestamp  
[Back to constructors index](/API_docs/constructors/index.html)



Whether people will be able to see our exact last online timestamp.

Note that if *we* decide to hide our exact last online timestamp to someone (i.e., users A, B, C, or all users) **and** we do not have a [Premium](https://core.telegram.org/api/premium) subscription, we won't be able to see the exact last online timestamp of those users (A, B, C, or all users), even if those users *do* share it with us.

If those users *do* share their exact online status with us, but we can't see it due to the reason mentioned above, the `by_me` flag of [userStatusRecently](../constructors/userStatusRecently.html), [userStatusLastWeek](../constructors/userStatusLastWeek.html), [userStatusLastMonth](../constructors/userStatusLastMonth.html) will be set.




### Type: [InputPrivacyKey](/API_docs/types/InputPrivacyKey.html)


### Example:

```
$inputPrivacyKeyStatusTimestamp = ['_' => 'inputPrivacyKeyStatusTimestamp'];
```  
