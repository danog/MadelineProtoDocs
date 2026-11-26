# messageActionSuggestedPostRefund

> A suggested post » was accepted and posted or scheduled, but either the channel deleted the posted/scheduled post before stars_suggested_post_age_min seconds have elapsed, or the user refunded the payment for the stars used to pay for the suggested post.

[Back to constructors index](/API_docs/constructors/index.html)



A [suggested post »](https://core.telegram.org/api/suggested-posts) was accepted and posted or scheduled, but either the channel deleted the posted/scheduled post before [stars\_suggested\_post\_age\_min](https://core.telegram.org/api/config#stars-suggested-post-age-min) seconds have elapsed, or the user refunded the payment for the stars used to pay for the suggested post.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|payer\_initiated|[Bool](/API_docs/types/Bool.html) | Optional|If set, the user refunded the payment for the stars used to pay for the suggested post.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSuggestedPostRefund = ['_' => 'messageActionSuggestedPostRefund', 'payer_initiated' => Bool];
```
