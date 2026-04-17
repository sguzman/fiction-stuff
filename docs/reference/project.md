



i want to write fiction but i want to use my savvy tech skills to organize it and my deep theoertical insight to structure its state and dynamics. im thinking of splitting up the fictional universe into toml files. i want a file for things like:
- background (culture, language, religion, other nations, does magic exist, history, etc.)
- setting (subset of background that serves as the environment for the story)
- characters (named characters, traits, gender, disposition, personality
- technical/rigorous systems at play (what sustains the setting; economics, trade, demographic shifts, taxation, accounting, businesses, hydrology, climate, environmental degredation)
- that all i can think off for now

what do you think

Thought for 5s
I think this is an excellent idea.

You are basically treating fiction as a modeled world instead of a pile of prose. That fits you very well. TOML is a strong choice because it is readable, diff-friendly, easy to parse, easy to validate, and pleasant to maintain by hand.

The bigger idea here is this:

Your story should not just be “text files about lore.”
It should be a stateful system with layers.

A good split is:

world substrate
Things that are broadly true whether or not the story happens.
This is your background layer.

local instantiated environment
The specific place and time where this story occurs.
This is your setting layer.

agents
People, institutions, factions, households, businesses, armies, churches.

systems and constraints
The machinery that makes the world resist fantasy handwaving:
food, water, taxes, inheritance, trade routes, credit, disease, transport, literacy, class mobility, military logistics.

narrative state
What is currently true at the beginning of the story and how it changes.

That last one is the piece most people miss.

Your current categories are good, but I would add two more that will matter a lot:

events

relations

Without them, your world becomes a static encyclopedia.

A cleaner structure
I would recommend something like this:

world/
  background.toml
  setting.toml
  systems.toml
  characters/
    alice.toml
    bishop_hernan.toml
    salt_guild.toml
  factions/
    crown.toml
    river_merchants.toml
  locations/
    capital.toml
    marsh_district.toml
  events/
    0001_famine.toml
    0002_tax_revolt.toml
  relations/
    character_links.toml
    faction_links.toml
  story/
    initial_state.toml
    arcs.toml
    scenes.toml
Why this is better
Because “background,” “setting,” and “characters” are not enough to model dynamics.

You also need:

Relations
Who depends on whom?
Who hates whom?
Who owes money?
Who is sleeping with whom?
Who is loyal to what?
Who has legal authority over whom?

Events
What changed the world?
What is changing now?
What shocks are propagating through the system?

Story state
At chapter 1, what is true?
At chapter 7, what has changed?
Who knows what?
What secrets remain hidden?

That lets you treat the fiction almost like a simulation.

A more rigorous conceptual split
Here is the most useful distinction:

Ontology
What kinds of things exist?

Example:

person

city

church

tax

river

guild

spell

disease

dynasty

State
What is currently true?

Example:

grain price doubled

Duke is in debt

river level is low

temple influence is rising

plague is active in south ward

Dynamics
What causes change?

Example:

drought lowers yields

low yields raise grain prices

high prices trigger unrest

unrest weakens tax collection

weak taxes reduce army pay

unpaid army raises coup risk

This is where your “deep theoretical insight” will shine most.
You should not just store facts. You should store causal structure.

My strongest recommendation
Do not make the files just descriptive prose.
Give them fields that can be inspected, cross-referenced, and computed.

For example, instead of:

[kingdom]
description = "A harsh desert kingdom with a proud military tradition."
do something more like:

[id]
value = "kingdom_serekh"

[government]
type = "monarchy"
succession = "patrilineal"
centralization = 0.74

[economy]
base = ["salt", "caravan_trade", "copper"]
coinage = true
tax_farming = true
state_granaries = false

[environment]
biome = "arid_steppe"
rainfall = "low"
river_dependence = 0.82

[religion]
dominant = "solar_cult"
pluralism = 0.21

[military]
professional_army = true
cavalry_strength = 0.78
naval_strength = 0.05

[stability]
famine_risk = 0.61
revolt_risk = 0.34
elite_fragmentation = 0.48
Now you have something you can reason over.

Your categories, slightly upgraded
1. Background
This should contain deep world truths.

Include:

cosmology

metaphysics

religion

language families

civilizational history

legal traditions

technological level

magic ontology, if any

major nations and ethnic blocs

ecological zones

calendar and timekeeping

This is the “physics plus civilization” layer.

2. Setting
This should be narrower and story-relevant.

Include:

exact region

time period

urban/rural profile

local political tensions

climate and season

local customs

immediate material conditions

active conflicts

what ordinary people are worried about right now

This is the playable slice of the world.

3. Characters
Good, but I would split this into:

character identity

character psychology

character resources

character social embedding

character arc state

For example:

goals

fears

loyalties

habits

skills

secrets

class position

debts

family links

current knowledge

current emotional pressure

A character is not just personality traits.
A character is a node in a pressure network.

4. Technical systems
This is the gold.
Most fiction is weak here.

Include:

agriculture and food supply

tax flow

household economics

labor structure

transportation friction

disease ecology

hydrology

trade bottlenecks

class reproduction

inheritance

military provisioning

religious legitimacy

literacy and record keeping

This is the part that makes a world feel heavy and real.

The biggest trap
Do not let the system become an excuse to avoid writing scenes.

A lot of smart people build lore engines and never produce fiction.

So I would enforce a rule:

Every world file should justify at least one scene, conflict, or choice.

If a file contains information that never pressures a character, it is probably ornamental.

A very good extra split
I would add:

themes.toml
What is the story actually about at a conceptual level?

Example:

decay of aristocracy

debt as moral corrosion

literacy and power

empire through bookkeeping

divine legitimacy vs administrative legitimacy

love under bureaucratic pressure

Then each major subsystem can be linked to themes.

That helps keep the rigorous worldbuilding from becoming spiritually empty.

I would also add constraints.toml
This file answers:
What can’t happen easily?

Examples:

travel between capitals takes 11 days minimum

women cannot inherit landed office in this region

magic cannot create calories

tax collection depends on scribal records

river shipping stops during late dry season

steel production requires imported charcoal

most peasants cannot read contracts

Constraints are story gold because they force plot shape.

Best mental model
Treat your fictional universe like a hybrid of:

database

simulation

ontology

legal archive

economic model

character graph

dramaturgical engine

That sounds grandiose, but it is exactly the kind of structure that can let you build unusually dense fiction.

Minimal viable schema
If you want to keep it simple at first, I would start with just these files:

background.toml
setting.toml
systems.toml
themes.toml
constraints.toml
characters.toml
factions.toml
locations.toml
relations.toml
events.toml
story_state.toml
That is enough to begin.

One important design principle
Separate:

timeless facts

current facts

changing facts

For example:

Background:

The kingdom uses temple-mediated legitimacy.

Current state:

The current king is weak and temple support is split.

Dynamic rule:

Failed harvests increase temple charity demand and weaken royal prestige.

That separation will make your world much easier to maintain.

My verdict
Yes, absolutely do this.

But do it as a causal fiction architecture, not just a folder of lore notes.

Your instinct is already pointing in the right direction:
you do not merely want to invent a world, you want to model its state and dynamics.

That is a very strong foundation for serious fiction.

Tweetable version:

Most fiction worldbuilding is decorative. Yours should be executable.

Do not just write lore. Write a world that can push back.

If you want, I can draft a clean TOML schema for all these files with example fields and IDs.


I forgot about narrative state! thats the most important part. effectively i see it working like checkpoints or start/end of scenes. i can change things like for a character lets say they have an attribute called hp (hitpoints) of 10. then next scene something happens and they now have 5. i basically invent/decide on what happened in between. this is perfect! i want to use toml for all of this

Thought for a couple of seconds
Yes — that is the key breakthrough.

What you are describing is not just lore management. It is stateful fiction.

You are treating narrative as a sequence of world-states, where scenes are transformations. That is an extremely powerful way to think.

The core idea
A scene is not just “some prose happened.”

A scene is:

an input state

a set of pressures/actions/revelations

an output state

So instead of only writing:

John was wounded in the ambush.

you can represent:

before scene: hp = 10

after scene: hp = 5

And then the prose is your artistic rendering of the transition.

That is beautiful because it separates:

what changed

from

how it felt and unfolded

That gives you control without killing creativity.

This is basically a narrative state machine
Not in a cold robotic way, but in a rigorous one.

Each scene can be thought of as:

S_n --> scene logic --> S_n+1
where S_n is the current world state and S_n+1 is the next state.

That means scenes can modify:

character health

trust

suspicion

wealth

social status

information known

injuries

location

faction strength

food supply

weather

legal standing

pregnancy

grief

political risk

military morale

So fiction becomes partially computable.

Even better: use both snapshots and deltas
I would strongly recommend two kinds of TOML files:

1. Snapshot files
These describe the full state at a checkpoint.

Example:

scene_id = "scene_004"
time = "Year 12, Late Autumn, Morning"

[characters.mara]
location = "north_road"
hp = 5
fatigue = 7
morale = 3
gold = 12
knows_about_traitor = true

[characters.ivan]
location = "north_road"
hp = 9
fatigue = 4
morale = 6
gold = 2
knows_about_traitor = false

[world]
rainfall = "heavy"
grain_price_index = 1.8
road_safety = 0.2
2. Delta files
These record only what changed during the scene.

Example:

scene_id = "scene_004"
from_checkpoint = "scene_003_end"
to_checkpoint = "scene_004_end"

[[changes]]
entity = "characters.mara"
field = "hp"
old = 10
new = 5
cause = "knife wound during ambush"

[[changes]]
entity = "characters.mara"
field = "knows_about_traitor"
old = false
new = true
cause = "overheard enemy conversation"

[[changes]]
entity = "world.road_safety"
field = "value"
old = 0.6
new = 0.2
cause = "bandit attack exposed route vulnerability"
This is ideal because:

snapshots are easy to inspect

deltas explain movement

you can reconstruct continuity

you can catch contradictions

This solves a huge fiction problem
Writers constantly lose track of:

who knows what

who is where

who is injured

what promises were made

what changed emotionally

whether a character should still be angry

whether a city should now be low on food

whether the passage of time makes sense

Your TOML state system gives you memory and continuity.

You should track more than physical stats
HP is a good example, but the real power comes when you track soft narrative variables too.

For a character, I would consider fields like:

hp

fatigue

stress

morale

trust_in_X

fear_of_X

loyalty

gold

social_exposure

wanted_level

secrets_known

lies_believed

injuries

relationships

location

goal

short_term_intent

For a faction or setting:

grain_stores

treasury

military_readiness

religious_unrest

plague_intensity

river_level

corruption_index

legitimacy

trade_flow

public_morale

That is where your theoretical instincts can do real work.

A very important distinction
You should distinguish between:

Persistent traits
These rarely change.

Examples:

height

sex

native language

baseline temperament

bloodline

education level

Dynamic state
These change scene by scene.

Examples:

hp

mood

suspicion

money

injuries

allegiance

knowledge

location

Derived state
These are computed from other things.

Examples:

combat readiness

marriage eligibility

famine risk

bankruptcy risk

scandal risk

This matters because otherwise your files become messy and redundant.

Best structure for TOML
I would separate:

characters/
  mara/
    static.toml
    state.toml
    history.toml
Or if you want scene-based snapshots:

story/
  checkpoints/
    0001_start.toml
    0002_end_of_market_scene.toml
    0003_after_ambush.toml
  deltas/
    0002_market_scene.toml
    0003_ambush.toml
That way you can inspect the whole story as a sequence of transitions.

You can even model knowledge state
This is one of the best uses.

Example:

[characters.mara.knowledge]
knows_king_is_dying = true
knows_letter_is_forged = false
knows_brother_survived = false
Then later:

[[changes]]
entity = "characters.mara.knowledge"
field = "knows_brother_survived"
old = false
new = true
cause = "read intercepted military ledger"
That means revelations become formal state changes.

That is huge, because plot often depends less on brute action than on information redistribution.

Emotional state matters too
You could track emotional dimensions numerically or categorically.

Example:

[characters.mara.emotional_state]
grief = 8
anger = 6
hope = 2
trust_in_ivan = 4
Then a reconciliation scene can formally alter those.

This helps because emotional arcs often get lost if they are not made explicit.

Your prose still matters
This system does not replace writing.

It gives you a scaffold for writing.

The prose answers:

how did hp go from 10 to 5?

was it sudden, humiliating, ironic, glorious?

did the character resist, panic, freeze?

what did it mean symbolically?

The TOML gives structural truth.
The prose gives aesthetic truth.

Both matter.

You may want “scene intent” too
For each scene, store not just changes, but what the scene is supposed to do.

Example:

scene_id = "scene_004"
purpose = [
  "injure_mara",
  "reveal_traitor_exists",
  "reduce_route_safety",
  "increase_ivan_guilt"
]
This helps you avoid flabby scenes.

A scene should have measurable narrative work.

You can also track continuity constraints
Example:

[constraints]
mara_cannot_fight = true
because = "broken rib"

ivan_cannot_leave_city = true
because = "under surveillance"
Then when you plan the next scene, you know what cannot plausibly happen.

This is almost like save files for fiction
And that is a good thing.

Not gamefication for its own sake, but continuity discipline.

You are making “save points” for your universe.

That lets you ask:

what changed?

why?

who caused it?

what should logically follow?

That is exactly how strong long-form fiction stays coherent.

One subtle warning
Do not over-quantize everything.

Some things work well as numbers:

hp

money

food

soldiers

travel time

water level

Some things work better as tags, sets, or categories:

injury type

social stigma

secrets known

legal status

vows made

traumatic memory

political alignment

For example, this is better than just a number:

[characters.mara.injuries]
wounded_arm = true
broken_rib = true
blood_loss = "moderate"
because it gives more writing texture.

Strong recommendation
Use this four-layer model:

1. Static ontology
What exists in the world.

2. Baseline world state
What is true at story start.

3. Scene delta
What each scene changes.

4. Checkpoint snapshot
What the resulting state is after the scene.

That is the cleanest architecture.

Tiny example
Character file
id = "mara"
name = "Mara Vale"
sex = "female"
culture = "riverland"
native_language = "valic"

[traits]
temperament = "guarded"
intelligence = "high"
courage = "uneven"
Initial state
[characters.mara]
hp = 10
gold = 4
location = "south_market"
trust_in_ivan = 6
knows_about_traitor = false
Scene delta
scene_id = "ambush_at_the_bridge"

[[changes]]
entity = "characters.mara"
field = "hp"
old = 10
new = 5

[[changes]]
entity = "characters.mara"
field = "knows_about_traitor"
old = false
new = true

[[changes]]
entity = "characters.mara"
field = "location"
old = "south_market"
new = "north_road"
Resulting checkpoint
checkpoint = "after_ambush"

[characters.mara]
hp = 5
gold = 4
location = "north_road"
trust_in_ivan = 4
knows_about_traitor = true
That is already enough to manage a serious narrative.

Final verdict
Yes. Fully commit to TOML.

What you have now is not merely a note-taking method.
It is a formal narrative state engine.

Tweetable version:

A scene is a state transition disguised as drama.

Lore tells you what exists. Narrative state tells you what changed.

I can sketch you a full TOML directory layout next, with example files for background, characters, systems, scene_deltas, and checkpoints.





