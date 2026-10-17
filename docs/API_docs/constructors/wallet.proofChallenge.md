---
title: "wallet.proofChallenge"
description: "wallet.proofChallenge attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/wallet_proofChallenge.html
---
# Constructor: wallet.proofChallenge  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|payload|[string](/API_docs/types/string.html) | Yes|
|expires|[int](/API_docs/types/int.html) | Yes|
|domain|[string](/API_docs/types/string.html) | Yes|



### Type: [wallet.ProofChallenge](/API_docs/types/wallet.ProofChallenge.html)


### Example:

```
$wallet_proofChallenge = ['_' => 'wallet.proofChallenge', 'payload' => 'string', 'expires' => int, 'domain' => 'string'];
```  
