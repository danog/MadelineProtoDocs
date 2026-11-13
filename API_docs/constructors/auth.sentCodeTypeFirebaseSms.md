# auth.sentCodeTypeFirebaseSms

> An authentication code should be delivered via SMS after Firebase attestation, as described in the auth documentation ».

[Back to constructors index](/API_docs/constructors/index.html)



An authentication code should be delivered via SMS after Firebase attestation, as described in the [auth documentation »](https://core.telegram.org/api/auth).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[bytes](/API_docs/types/bytes.html) | Optional|On Android, the nonce to be used as described in the [auth documentation »](https://core.telegram.org/api/auth)|
|play\_integrity\_project\_id|[long](/API_docs/types/long.html) | Optional|Google Play Integrity project ID|
|play\_integrity\_nonce|[bytes](/API_docs/types/bytes.html) | Optional|Play Integrity API nonce|
|receipt|[string](/API_docs/types/string.html) | Optional|On iOS, must be compared with the `receipt` extracted from the received push notification.|
|push\_timeout|[int](/API_docs/types/int.html) | Optional|On iOS: if a push notification with the `ios_push_secret` isn't received within `push_timeout` seconds, the `next_type` authentication method must be used, with [auth.resendCode](../methods/auth.resendCode.html).|
|length|[int](/API_docs/types/int.html) | Yes|Length of the code that will be delivered.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeFirebaseSms = ['_' => 'auth.sentCodeTypeFirebaseSms', 'nonce' => 'bytes', 'play_integrity_project_id' => long, 'play_integrity_nonce' => 'bytes', 'receipt' => 'string', 'push_timeout' => int, 'length' => int];
```
