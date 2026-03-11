# ByteBites UML Class Diagram

```
┌─────────────────────┐
│      Customer       │
├─────────────────────┤
│ - name: string      │
│ - purchaseHistory   │
├─────────────────────┤
│ (verification)      │
└──────────┬──────────┘
           │ places
           │ 1..*
           ▼
┌─────────────────────┐       contains *     ┌─────────────────────┐
│       Order         │◄─────────────────────│     FoodItem        │
├─────────────────────┤                      ├─────────────────────┤
│ - selectedItems     │                      │ - name: string      │
├─────────────────────┤                      │ - price: number     │
│ + getTotalCost()    │                      │ - category: string  │
└─────────────────────┘                      │ - popularityRating  │
           │                                 └──────────┬──────────┘
           │ contains *                                │
           └───────────────────────────────────────────┘
                                                       │
                                                       │ 1..*
                                                       │
                                                       ▼
           ┌─────────────────────┐
           │       Menu          │
           ├─────────────────────┤
           │ - items: FoodItem[] │
           ├─────────────────────┤
           │ + filterByCategory()│
           └─────────────────────┘
```

| Class | Attributes | Methods |
|-------|------------|---------|
| **Customer** | `name`, `purchaseHistory` | (verification) |
| **FoodItem** | `name`, `price`, `category`, `popularityRating` | — |
| **Menu** | `items` (collection of FoodItem) | `filterByCategory()` |
| **Order** | `selectedItems` | `getTotalCost()` |
