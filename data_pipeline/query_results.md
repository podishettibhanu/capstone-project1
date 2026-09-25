# SQL Query Results

## Query 1 — WHERE

```sql
SELECT title, price_gbp
        FROM books
        WHERE price_gbp > 30;
```

### Output

| title                                                                                                                                                                           |   price_gbp |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------:|
| A Light in the Attic                                                                                                                                                            |       51.77 |
| Tipping the Velvet                                                                                                                                                              |       53.74 |
| Soumission                                                                                                                                                                      |       50.1  |
| Sharp Objects                                                                                                                                                                   |       47.82 |
| Sapiens: A Brief History of Humankind                                                                                                                                           |       54.23 |
| The Dirty Little Secrets of Getting Your Dream Job                                                                                                                              |       33.34 |
| The Black Maria                                                                                                                                                                 |       52.15 |
| Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)                                                                                                                         |       52.29 |
| Rip it Up and Start Again                                                                                                                                                       |       35.02 |
| Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991                                                                                              |       57.25 |
| Mesaerion: The Best Science Fiction Stories 1800-1849                                                                                                                           |       37.59 |
| Libertarianism for Beginners                                                                                                                                                    |       51.33 |
| It's Only the Himalayas                                                                                                                                                         |       45.17 |
| How Music Works                                                                                                                                                                 |       37.32 |
| Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More |       30.52 |
| Black Dust                                                                                                                                                                      |       34.53 |
| Birdsong: A Story in Pictures                                                                                                                                                   |       54.64 |
| Aladdin and His Wonderful Lamp                                                                                                                                                  |       53.13 |
| Worlds Elsewhere: Journeys Around Shakespeareâs Globe                                                                                                                         |       40.3  |
| Wall and Piece                                                                                                                                                                  |       44.18 |
| The Five Love Languages: How to Express Heartfelt Commitment to Your Mate                                                                                                       |       31.05 |
| The Bear and the Piano                                                                                                                                                          |       36.89 |
| Penny Maybe                                                                                                                                                                     |       33.29 |
| Behind Closed Doors                                                                                                                                                             |       52.22 |
| You can't bury them all: Poems                                                                                                                                                  |       33.63 |
| Slow States of Collapse: Poems                                                                                                                                                  |       57.31 |
| Private Paris (Private #10)                                                                                                                                                     |       47.61 |
| Without Borders (Wanderlove #1)                                                                                                                                                 |       45.07 |
| When We Collided                                                                                                                                                                |       31.77 |
| We Love You, Charlie Freeman                                                                                                                                                    |       50.27 |
| Unseen City: The Majesty of Pigeons, the Discreet Charm of Snails & Other Wonders of the Urban Wilderness                                                                       |       44.18 |
| Throwing Rocks at the Google Bus: How Growth Became the Enemy of Prosperity                                                                                                     |       31.12 |
| The Secret of Dreadwillow Carse                                                                                                                                                 |       56.13 |
| The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper!                                                 |       56.41 |
| The Past Never Ends                                                                                                                                                             |       56.5  |
| The Natural History of Us (The Fine Art of Pretending #2)                                                                                                                       |       45.22 |
| The Nameless City (The Nameless City #1)                                                                                                                                        |       38.16 |
| The Murder That Never Was (Forensic Instincts #5)                                                                                                                               |       54.11 |
| The Most Perfect Thing: Inside (and Outside) a Bird's Egg                                                                                                                       |       42.96 |
| The Gutsy Girl: Escapades for Your Life of Epic Adventure                                                                                                                       |       37.13 |
| The Electric Pencil: Drawings from Inside State Hospital No. 3                                                                                                                  |       56.06 |
| The Death of Humanity: and the Case for Life                                                                                                                                    |       58.11 |
| The Bulletproof Diet: Lose up to a Pound a Day, Reclaim Energy and Focus, Upgrade Your Life                                                                                     |       49.05 |
| The Art Forger                                                                                                                                                                  |       40.76 |
| The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution                                                                                                             |       32.24 |
| Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up                                                                                                  |       41.83 |
| Soul Reader                                                                                                                                                                     |       39.58 |
| Security                                                                                                                                                                        |       39.25 |
| Saga, Volume 5 (Saga (Collected Editions) #5)                                                                                                                                   |       51.04 |
| Rat Queens, Vol. 3: Demons (Rat Queens (Collected Editions) #11-15)                                                                                                             |       50.4  |
| Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics             |       36.28 |
| orange: The Complete Collection 1 (orange: The Complete Collection #1)                                                                                                          |       48.41 |
| Online Marketing for Busy Authors: A Step-By-Step Guide                                                                                                                         |       46.35 |
| My Paris Kitchen: Recipes and Stories                                                                                                                                           |       33.37 |
| Masks and Shadows                                                                                                                                                               |       56.4  |
| Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)                                                                                                                   |       46.91 |
| Lumberjanes, Vol. 1: Beware the Kitten Holy (Lumberjanes #1-4)                                                                                                                  |       45.61 |
| Layered: Baking, Building, and Styling Spectacular Cakes                                                                                                                        |       40.11 |
| Judo: Seven Steps to Black Belt (an Introductory Guide for Beginners)                                                                                                           |       53.9  |
| Join                                                                                                                                                                            |       35.67 |

## Query 2 — ORDER BY and LIMIT

```sql
SELECT title, price_gbp
        FROM books
        ORDER BY price_gbp DESC
        LIMIT 10;
```

### Output

| title                                                                                                                           |   price_gbp |
|:--------------------------------------------------------------------------------------------------------------------------------|------------:|
| The Death of Humanity: and the Case for Life                                                                                    |       58.11 |
| Slow States of Collapse: Poems                                                                                                  |       57.31 |
| Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991                                              |       57.25 |
| The Past Never Ends                                                                                                             |       56.5  |
| The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper! |       56.41 |
| Masks and Shadows                                                                                                               |       56.4  |
| The Secret of Dreadwillow Carse                                                                                                 |       56.13 |
| The Electric Pencil: Drawings from Inside State Hospital No. 3                                                                  |       56.06 |
| Birdsong: A Story in Pictures                                                                                                   |       54.64 |
| Sapiens: A Brief History of Humankind                                                                                           |       54.23 |

## Query 3 — DISTINCT

```sql
SELECT DISTINCT star_rating
        FROM books
        ORDER BY star_rating;
```

### Output

|   star_rating |
|--------------:|
|             1 |
|             2 |
|             3 |
|             4 |
|             5 |

## Query 4 — BETWEEN

```sql
SELECT title, price_gbp, star_rating
        FROM books
        WHERE price_gbp BETWEEN 10 AND 20;
```

### Output

| title                                                                                   |   price_gbp |   star_rating |
|:----------------------------------------------------------------------------------------|------------:|--------------:|
| The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull |       17.93 |             3 |
| Starving Hearts (Triangular Trade Trilogy, #1)                                          |       13.99 |             2 |
| Set Me Free                                                                             |       17.46 |             5 |
| In Her Wake                                                                             |       12.84 |             1 |
| The Four Agreements: A Practical Guide to Personal Freedom                              |       17.66 |             5 |
| Sophie's World                                                                          |       15.94 |             5 |
| Maude (1883-1993):She Grew Up with the country                                          |       18.02 |             2 |
| In a Dark, Dark Wood                                                                    |       19.63 |             1 |
| Untitled Collection: Sabbath Poems 2014                                                 |       14.27 |             4 |
| Unicorn Tracks                                                                          |       18.78 |             3 |
| Tsubasa: WoRLD CHRoNiCLE 2 (Tsubasa WoRLD CHRoNiCLE #2)                                 |       16.28 |             1 |
| This One Summer                                                                         |       19.49 |             4 |
| Thirst                                                                                  |       17.27 |             5 |
| The Torch Is Passed: A Harding Family Story                                             |       19.09 |             1 |
| The Life-Changing Magic of Tidying Up: The Japanese Art of Decluttering and Organizing  |       16.77 |             3 |
| The Age of Genius: The Seventeenth Century and the Birth of the Modern Mind             |       19.73 |             1 |
| Reskilling America: Learning to Labor in the Twenty-First Century                       |       19.83 |             2 |
| Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish 2-in-1 Omnibus #1)       |       13.61 |             5 |
| Princess Between Worlds (Wide-Awake Princess #5)                                        |       13.34 |             5 |
| Pop Gun War, Volume 1: Gift                                                             |       18.97 |             1 |
| Patience                                                                                |       10.16 |             3 |
| Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)                                  |       15.44 |             4 |
| On a Midnight Clear                                                                     |       14.07 |             3 |
| Obsidian (Lux #1)                                                                       |       14.86 |             2 |
| Mama Tried: Traditional Italian Cooking for the Screwed, Crude, Vegan, and Tattooed     |       14.02 |             4 |
| Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)                                 |       19.92 |             2 |

## Query 5 — IN

```sql
SELECT title, price_gbp, price_inr
        FROM books
        WHERE star_rating IN (4, 5);
```

### Output

| title                                                                                                                                                  |   price_gbp |   price_inr |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------|------------:|------------:|
| Sharp Objects                                                                                                                                          |       47.82 |     5045.01 |
| Sapiens: A Brief History of Humankind                                                                                                                  |       54.23 |     5721.26 |
| The Dirty Little Secrets of Getting Your Dream Job                                                                                                     |       33.34 |     3517.37 |
| The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics                                                         |       22.6  |     2384.3  |
| Shakespeare's Sonnets                                                                                                                                  |       20.66 |     2179.63 |
| Set Me Free                                                                                                                                            |       17.46 |     1842.03 |
| Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)                                                                                                |       52.29 |     5516.6  |
| Rip it Up and Start Again                                                                                                                              |       35.02 |     3694.61 |
| Chase Me (Paris Nights #2)                                                                                                                             |       25.27 |     2665.99 |
| Black Dust                                                                                                                                             |       34.53 |     3642.91 |
| Worlds Elsewhere: Journeys Around Shakespeareâs Globe                                                                                                |       40.3  |     4251.65 |
| Wall and Piece                                                                                                                                         |       44.18 |     4660.99 |
| The Four Agreements: A Practical Guide to Personal Freedom                                                                                             |       17.66 |     1863.13 |
| The Elephant Tree                                                                                                                                      |       23.82 |     2513.01 |
| Sophie's World                                                                                                                                         |       15.94 |     1681.67 |
| Behind Closed Doors                                                                                                                                    |       52.22 |     5509.21 |
| Private Paris (Private #10)                                                                                                                            |       47.61 |     5022.85 |
| #HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.                                                                                     |       23.11 |     2438.11 |
| We Love You, Charlie Freeman                                                                                                                           |       50.27 |     5303.49 |
| Untitled Collection: Sabbath Poems 2014                                                                                                                |       14.27 |     1505.48 |
| Unseen City: The Majesty of Pigeons, the Discreet Charm of Snails & Other Wonders of the Urban Wilderness                                              |       44.18 |     4660.99 |
| This One Summer                                                                                                                                        |       19.49 |     2056.2  |
| Thirst                                                                                                                                                 |       17.27 |     1821.98 |
| The Past Never Ends                                                                                                                                    |       56.5  |     5960.75 |
| The Nameless City (The Nameless City #1)                                                                                                               |       38.16 |     4025.88 |
| The Most Perfect Thing: Inside (and Outside) a Bird's Egg                                                                                              |       42.96 |     4532.28 |
| The Mindfulness and Acceptance Workbook for Anxiety: A Guide to Breaking Free from Anxiety, Phobias, and Worry Using Acceptance and Commitment Therapy |       23.89 |     2520.39 |
| The Inefficiency Assassin: Time Management Tactics for Working Smarter, Not Longer                                                                     |       20.59 |     2172.24 |
| The Death of Humanity: and the Case for Life                                                                                                           |       58.11 |     6130.6  |
| The Activist's Tao Te Ching: Ancient Advice for a Modern Revolution                                                                                    |       32.24 |     3401.32 |
| Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up                                                                         |       41.83 |     4413.06 |
| Princess Jellyfish 2-in-1 Omnibus, Vol. 01 (Princess Jellyfish 2-in-1 Omnibus #1)                                                                      |       13.61 |     1435.86 |
| Princess Between Worlds (Wide-Awake Princess #5)                                                                                                       |       13.34 |     1407.37 |
| Outcast, Vol. 1: A Darkness Surrounds Him (Outcast #1)                                                                                                 |       15.44 |     1628.92 |
| Mama Tried: Traditional Italian Cooking for the Screwed, Crude, Vegan, and Tattooed                                                                    |       14.02 |     1479.11 |
| Join                                                                                                                                                   |       35.67 |     3763.18 |
| In the Country We Love: My Family Divided                                                                                                              |       22    |     2321    |

## Query 6 — JOIN

```sql
SELECT
            books.title,
            books.price_gbp,
            books.price_inr,
            books.star_rating,
            categories.category_name
        FROM books
        JOIN categories
        ON books.category_id = categories.category_id
        ORDER BY books.price_inr DESC
        LIMIT 10;
```

### Output

| title                                                                                                                           |   price_gbp |   price_inr |   star_rating | category_name   |
|:--------------------------------------------------------------------------------------------------------------------------------|------------:|------------:|--------------:|:----------------|
| The Death of Humanity: and the Case for Life                                                                                    |       58.11 |     6130.6  |             4 | Philosophy      |
| Slow States of Collapse: Poems                                                                                                  |       57.31 |     6046.2  |             3 | Poetry          |
| Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991                                              |       57.25 |     6039.88 |             3 | Music           |
| The Past Never Ends                                                                                                             |       56.5  |     5960.75 |             4 | Mystery         |
| The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper! |       56.41 |     5951.25 |             1 | Food and Drink  |
| Masks and Shadows                                                                                                               |       56.4  |     5950.2  |             2 | Fantasy         |
| The Secret of Dreadwillow Carse                                                                                                 |       56.13 |     5921.72 |             1 | Childrens       |
| The Electric Pencil: Drawings from Inside State Hospital No. 3                                                                  |       56.06 |     5914.33 |             1 | Nonfiction      |
| Birdsong: A Story in Pictures                                                                                                   |       54.64 |     5764.52 |             3 | Childrens       |
| Sapiens: A Brief History of Humankind                                                                                           |       54.23 |     5721.26 |             5 | History         |

## pandas.merge Result

| title                                                                                                                           |   price_gbp |   price_inr |   star_rating | category_name   |
|:--------------------------------------------------------------------------------------------------------------------------------|------------:|------------:|--------------:|:----------------|
| The Death of Humanity: and the Case for Life                                                                                    |       58.11 |     6130.6  |             4 | Philosophy      |
| Slow States of Collapse: Poems                                                                                                  |       57.31 |     6046.2  |             3 | Poetry          |
| Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991                                              |       57.25 |     6039.88 |             3 | Music           |
| The Past Never Ends                                                                                                             |       56.5  |     5960.75 |             4 | Mystery         |
| The Pioneer Woman Cooks: Dinnertime: Comfort Classics, Freezer Food, 16-Minute Meals, and Other Delicious Ways to Solve Supper! |       56.41 |     5951.25 |             1 | Food and Drink  |
| Masks and Shadows                                                                                                               |       56.4  |     5950.2  |             2 | Fantasy         |
| The Secret of Dreadwillow Carse                                                                                                 |       56.13 |     5921.72 |             1 | Childrens       |
| The Electric Pencil: Drawings from Inside State Hospital No. 3                                                                  |       56.06 |     5914.33 |             1 | Nonfiction      |
| Birdsong: A Story in Pictures                                                                                                   |       54.64 |     5764.52 |             3 | Childrens       |
| Sapiens: A Brief History of Humankind                                                                                           |       54.23 |     5721.26 |             5 | History         |
