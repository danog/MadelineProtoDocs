---
title: "starsSubscription"
description: "Represents a Telegram Star subscription »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsSubscription  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [Telegram Star subscription »](https://core.telegram.org/api/invites#paid-invite-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|canceled|[Bool](/API_docs/types/Bool.html) | Optional|Whether this subscription was cancelled.|
|can\_refulfill|[Bool](/API_docs/types/Bool.html) | Optional|Whether we left the associated private channel, but we can still rejoin it using [payments.fulfillStarsSubscription](../methods/payments.fulfillStarsSubscription.html) because the current subscription period hasn't expired yet.|
|missing\_balance|[Bool](/API_docs/types/Bool.html) | Optional|Whether this subscription has expired because there are not enough stars on the user's balance to extend it.|
|bot\_canceled|[Bool](/API_docs/types/Bool.html) | Optional|Set if this [bot subscription](https://core.telegram.org/api/subscriptions#bot-subscriptions) was cancelled by the bot|
|id|[string](/API_docs/types/string.html) | Yes|Subscription ID.|
|peer|[long](/API_docs/types/long.html) | Yes|Identifier of the associated private chat.|
|until\_date|[int](/API_docs/types/int.html) | Yes|Expiration date of the current subscription period.|
|pricing|[StarsSubscriptionPricing](/API_docs/types/StarsSubscriptionPricing.html) | Yes|Pricing of the subscription in Telegram Stars.|
|chat\_invite\_hash|[string](/API_docs/types/string.html) | Optional|Invitation link, used to renew the subscription after cancellation or expiration.|
|title|[string](/API_docs/types/string.html) | Optional|For bot subscriptions, the title of the subscription invoice|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|For bot subscriptions, the photo from the subscription invoice|
|invoice\_slug|[string](/API_docs/types/string.html) | Optional|For bot subscriptions, the [identifier](https://core.telegram.org/api/links#invoice-links) of the subscription invoice|



### Type: [StarsSubscription](/API_docs/types/StarsSubscription.html)


### Example:

```
$starsSubscription = ['_' => 'starsSubscription', 'canceled' => Bool, 'can_refulfill' => Bool, 'missing_balance' => Bool, 'bot_canceled' => Bool, 'id' => 'string', 'peer' => long, 'until_date' => int, 'pricing' => StarsSubscriptionPricing, 'chat_invite_hash' => 'string', 'title' => 'string', 'photo' => WebDocument, 'invoice_slug' => 'string'];
```  
