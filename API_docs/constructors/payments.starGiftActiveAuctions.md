# payments.starGiftActiveAuctions

> payments.starGiftActiveAuctions attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|auctions|Array of [StarGiftActiveAuctionState](/API_docs/types/StarGiftActiveAuctionState.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|



### Type: [payments.StarGiftActiveAuctions](/API_docs/types/payments.StarGiftActiveAuctions.html)


### Example:

```
$payments_starGiftActiveAuctions = ['_' => 'payments.starGiftActiveAuctions', 'auctions' => [StarGiftActiveAuctionState, StarGiftActiveAuctionState], 'users' => [User, User], 'chats' => [Chat, Chat]];
```
