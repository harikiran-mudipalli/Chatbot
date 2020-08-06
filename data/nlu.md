## intent:main_menu
- Let's see
- Main menu
- menu

## intent: travel_menu
- travel menu

## intent:travel_best_valued_packages
- plan my trip

## intent:pet_bool
- do you plan to bring [pets](pets)
- are there any [pets](pets) you wish to bring

## intent:travel_packages_by_interest
- packages based on interest

## intent:travel_packages_by_budget
- packages based on budget

## intent:property_type
- property type

## intent:Modify_cancel_Booking
- [cancel my booking](modify_booking)
- [change my booking](modify_booking)
- [modify my booking](modify_booking)

## intent:faq
- go to faq
- faq

##intent:get_live_assistance
- get live assistance
- get live support
- pass on to human 

## intent:property_booking_menu
- book a property
- show me the properties available

## intent:greet
- [hey](greeting)
- [hello](greeting)
- [hi](greeting)
- [good morning](greeting)
- [good evening](greeting)
- [hey there](greeting)

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent: stop
  examples: |
    - ok then you cant help me
    - that was shit, you're not helping
    - you can't help me
    - you can't help me with what i need
    - i guess you can't help me then
    - ok i guess you can't help me
    - that's not what i want
    - ok, but that doesnt help me
    - this is leading to nothing
    - this conversation is not really helpful
    - you cannot help me with what I want
    - I think you cant help me
    - hm i don't think you can do what i want
    - stop
    - stop go back
    - do you get anything?
    - and you call yourself bot company? pff
    - and that's it?
    - nothing else?

## intent: value_correction
- I want to [change my destination](change_destination) to [New York](destination)
- can I [change my destination](change_destination) to [Barcelona](destination)?
- can you [change my destination](change_destination) to [Athens](destination)?
- Please [change my destination](change_destination) to [Sydney](destination)
- I would like to [update my destination](change_destination) to [Havana](destination)
- [change my destination](change_destination) to [Paris](destination)
- [update my destination](change_destination) to [Doha](destination)
- [change my destination](change_destination) to [Amsterdam](destination)
- [change my destination](change_destination) to [Venice](destination)
- [change my destination](change_destination) to [Kyoto](destination)

- I want to [change my boarding point](change_origin) to [Hyderabad](origin)
- can I [change my boarding point](change_origin) to [Chennai](origin)?
- can you [change my boarding point](change_origin) to [Delhi](origin)?
- Please [update my boarding point](change_origin) to [Kolkata](origin)
- I would like to [change my boarding point](change_origin) to [Mumbai](origin)
- [change my boarding point](change_origin) to [Goa](origin)
- [change my boarding point](change_origin) to [Cape Town](origin)
- [change my boarding point](change_origin) to [Budapest](origin)
- [update my boarding point](change_origin) to [Lisbon](origin)
- [change my boarding point](change_origin) to [Istanbul](origin)

- [change adults count](change_adults_count) to [3](adults_count)
- Can you [change adults count](change_adults_count) to [1](adults_count)
- [change adults count](change_adults_count) to [2](adults_count)
- Can you [change adults count](change_adults_count) to [4](adults_count)
- [change adults count](change_adults_count) to [5](adults_count)
- Can you [change adults count](change_adults_count) to [6](adults_count)
- [change adults count](change_adults_count) to [7](adults_count)
- Can you [change adults count](change_adults_count) to [8](adults_count)
- [change children count](change_children_count) to [9](adults_count)
- Can you [change adults count](change_adults_count) to [10](adults_count)

- [change children count](change_children_count) to [5](child_count)
- Can you [change children count](change_children_count) to [10](child_count)
- [change children count](change_children_count) to [1](child_count)
- Can you [change children count](change_children_count) to [0](child_count)
- [change children count](change_children_count) to [2](child_count)
- Can you [change children count](change_children_count) to [3](child_count)
- [change children count](change_children_count) to [4](child_count)
- Can you [change children count](change_children_count) to [6](child_count)
- [change children count](change_children_count) to [7](child_count)
- Can you [change children count](change_children_count) to [8](child_count)

- [change travel date](change_travel_date) to [11/11/23](travel_date)
- [change travel period](change_travel_period) to [12](travel_period)
- [change budget](change_budget) to [2000](budget)

## intent: amenities
- [2](bedroom) [1](bathroom)

## intent: facilities
- [wifi](wifi) [pool](pool)

## lookup:countries
- data/countries.txt

## regex:number
- [0-9]{1,10}

## regex:date_format
-[0-9]{2}/[0-9]{2}/[0-9]{4}

