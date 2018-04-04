---
title: temporaryPasswordState
description: Returns information about availability of temporary password, which should be used for payments
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: temporaryPasswordState  
[Back to constructors index](index.md)



Returns information about availability of temporary password, which should be used for payments

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_password|[Bool](../types/Bool.md) | Yes|True, if we have temporary password|
|valid\_for|[int](../types/int.md) | Yes|Time left before temporary password expires, seconds|



### Type: [TemporaryPasswordState](../types/TemporaryPasswordState.md)


