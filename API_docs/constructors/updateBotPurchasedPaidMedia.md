# updateBotPurchasedPaidMedia

> Bots only: a user has purchased a paid media.

[Back to constructors index](/API_docs/constructors/index.html)



Bots only: a user has purchased a [paid media](https://core.telegram.org/api/paid-media).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|The user that bought the media|
|payload|[string](/API_docs/types/string.html) | Yes|Payload passed by the bot in [inputMediaPaidMedia](../constructors/inputMediaPaidMedia.html).`payload`|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotPurchasedPaidMedia = ['_' => 'updateBotPurchasedPaidMedia', 'user_id' => long, 'payload' => 'string', 'qts' => int];
```
