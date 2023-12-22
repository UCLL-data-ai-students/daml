# student manual

| Column Name          | Description                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| SalesID              | Unique identifier for each sale.                                                                  |
| Age                  | Age of the traveler.                                                                              |
| Country              | Country of origin of the traveler.                                                                |
| Membership_Status    | Membership level of the traveler in the booking system; could be 'standard', 'silver', or 'gold'. |
| Previous_Purchases   | Number of previous bookings made by the traveler.                                                 |
| Destination          | Travel destination chosen by the traveler.                                                        |
| Stay_length          | Duration of stay at the destination.                                                              |
| Guests               | Number of guests traveling with the primary traveler.                                             |
| Travel_month         | Month in which the travel is scheduled.                                                           |
| Months_before_travel | Number of months prior to travel that the booking was made.                                       |
| Earlybird_discount   | Boolean flag indicating whether the traveler received an early bird discount.                     |
| Package_Type         | Type of travel package chosen by the traveler.                                                    |
| Cost                 | Calculated cost of the travel package.                                                            |

# instructor manual

| Column Name          | Data Generation Description                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Age                  | Generated using a normal distribution centered around 40 with a standard deviation of 15. Restricted between 18 to 80. |
| Country              | Chosen randomly from a predefined list of countries.                                                                   |
| Membership_Status    | Chosen randomly from 'standard', 'silver', or 'gold' with respective probabilities of 0.5, 0.3, and 0.2.               |
| Previous_Purchases   | Generated using a Poisson distribution with a mean of 3.                                                               |
| Destination          | Chosen randomly from a predefined list of destinations.                                                                |
| Stay_length          | Generated using a gamma distribution with shape = 2 and scale = 5.                                                     |
| Guests               | Generated using a Poisson distribution with a mean of 1.5, added to 1, and clipped between 1 and 5.                    |
| Travel_month         | Generated using a bimodal distribution favoring summer (June, July, August) and winter (December, January, February).  |
| Months_before_travel | Generated using an exponential distribution with a scale of 3, and increased by 1.                                     |
| Earlybird_discount   | Generated based on a probability distribution with a 30% chance of being true.                                         |
| Package_Type         | Chosen randomly from predefined package types.                                                                         |
| Cost                 | Derived from stay length, subjected to random noise, and further modified based on travel month and package type.      |
|                      |


| Column Name              | Relationship & Contents Description                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Age                      | Affects cost based on package type and destination. Influences preference for 'Adventure' or 'Relaxation' packages.                                     |
| Country                  | The country of origin for the traveler.                                                                                                                 |
| Membership_Status        | Influences the number of previous purchases and traveler's ratings. Gold members get adjustments for prior purchases and ratings.                       |
| Previous_Purchases       | Number of prior purchases. Adjusted based on membership status.                                                                                         |
| Destination              | Choice of place to visit. Influences cost and profit margin. Some destinations are associated with specific package types, leading to cost adjustments. |
| Stay_length              | Directly impacts the base cost of the package. Longer stays are more expensive.                                                                         |
| Guests                   | Directly increases the overall cost, but does not affect the choice of destination.                                                                     |
| Travel_month             | Influences the cost of the package based on the peak season.                                                                                            |
| Months_before_travel     | Indicates when the booking was made relative to the travel date. Affects the likelihood of availing the early bird discount.                            |
| Earlybird_discount       | Can reduce the overall package cost. Directly tied to the 'Months_before_travel' column.                                                                |
| Package_Type             | Directly modifies the overall cost. There are relationships between age, destination, and package type, leading to cost adjustments.                    |
| Cost                     | Derived from multiple columns like 'Stay_length', 'Destination', 'Package_Type', etc.                                                                   |
| Rating                   | Derived based on the age of the traveler and their package preference. Adjusted for gold members.                                                       |
| Margin                   | Represents the profit margin. Derived from 'Cost' and adjusted for certain destinations.                                                                |
| Additional_Services_Cost | Derived from the 'Cost' column and adjusted based on the package type.                                                                                  |
