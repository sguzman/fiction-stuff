import os
import shutil
from pathlib import Path
import tomli_w

base_dir = Path("/win/linux/Code/Text/fiction-stuff")
examples_dir = base_dir / "data" / "examples" / "monster_blood"
dirs = ["agents_and_entities", "dynamics_and_rules", "narrative_state", "world_and_lore"]

for d in dirs:
    (examples_dir / d).mkdir(parents=True, exist_ok=True)

# Data to generate
agents = {
    "evan": {
        "main": {
            "id": "evan_ross",
            "name": "Evan Ross",
            "aliases": [],
            "birth_year": 1980,
            "components": {
                "physical": "evan.character_physical.toml",
                "psychology": "evan.character_psychology.toml"
            }
        },
        "physical": {
            "id": "evan_ross",
            "species": "Human",
            "gender": "Male",
            "description": "A twelve-year-old boy, often feels out of place, slightly small for his age.",
            "health": 100,
            "inventory": ["Monster Blood can"]
        },
        "psychology": {
            "id": "evan_ross",
            "traits": ["Anxious", "Curious", "Brave when pushed"],
            "motivations": ["Survive staying with his weird aunt", "Protect his dog Trigger", "Figure out what is wrong with the Monster Blood"],
            "fears": ["Aunt Kathryn", "Sarabeth", "The growing Monster Blood"]
        }
    },
    "andy": {
        "main": {
            "id": "andy",
            "name": "Andrea 'Andy'",
            "aliases": ["Andy"],
            "birth_year": 1980,
            "components": {
                "physical": "andy.character_physical.toml",
                "psychology": "andy.character_psychology.toml"
            }
        },
        "physical": {
            "id": "andy",
            "species": "Human",
            "gender": "Female",
            "description": "Tough girl from the neighborhood, often wears jeans and t-shirts, athletic.",
            "health": 100,
            "inventory": []
        },
        "psychology": {
            "id": "andy",
            "traits": ["Outgoing", "Adventurous", "Loyal"],
            "motivations": ["Have fun", "Solve mysteries with Evan"],
            "fears": ["Being swallowed by Monster Blood"]
        }
    },
    "kathryn": {
        "main": {
            "id": "aunt_kathryn",
            "name": "Aunt Kathryn",
            "aliases": [],
            "birth_year": 1920,
            "components": {
                "physical": "kathryn.character_physical.toml",
                "psychology": "kathryn.character_psychology.toml"
            }
        },
        "physical": {
            "id": "aunt_kathryn",
            "species": "Human",
            "gender": "Female",
            "description": "Tall, imposing older woman. Completely deaf. Often wears strange clothing. Uses sign language.",
            "health": 80,
            "inventory": []
        },
        "psychology": {
            "id": "aunt_kathryn",
            "traits": ["Strict", "Mysterious", "Misunderstood"],
            "motivations": ["Take care of Evan", "Protect her household"],
            "fears": ["Sarabeth's magic"]
        }
    },
    "sarabeth": {
        "main": {
            "id": "sarabeth",
            "name": "Sarabeth",
            "aliases": ["The Black Cat"],
            "birth_year": 1800,
            "components": {
                "physical": "sarabeth.character_physical.toml",
                "psychology": "sarabeth.character_psychology.toml"
            }
        },
        "physical": {
            "id": "sarabeth",
            "species": "Entity (Witch / Cat)",
            "gender": "Female",
            "description": "Usually appears as a large black cat with glowing eyes. True form is an ancient, evil witch.",
            "health": 200,
            "inventory": []
        },
        "psychology": {
            "id": "sarabeth",
            "traits": ["Malevolent", "Manipulative", "Cunning"],
            "motivations": ["Control Aunt Kathryn", "Cause chaos", "Destroy Evan"],
            "fears": ["Being outsmarted", "Losing her magical form"]
        }
    },
    "monster_blood": {
        "main": {
            "id": "monster_blood",
            "name": "Monster Blood",
            "aliases": ["The Green Slime"],
            "birth_year": 0,
            "components": {
                "physical": "monster_blood.character_physical.toml"
            }
        },
        "physical": {
            "id": "monster_blood",
            "species": "Magical Slime",
            "gender": "None",
            "description": "A pulsing, glowing green slime that expands exponentially when it consumes anything.",
            "health": 9999,
            "inventory": []
        }
    }
}

events = [
    {
        "id": "evt_arrival",
        "name": "Evan arrives in Atlanta",
        "type": "plot_point",
        "timestamp": 1,
        "description": "Evan Ross is dropped off by his parents to stay with his deaf, eccentric Aunt Kathryn while they house-hunt in Atlanta. He brings his cocker spaniel, Trigger.",
        "participants": ["evan_ross", "aunt_kathryn"]
    },
    {
        "id": "evt_toy_store",
        "name": "Buying Monster Blood",
        "type": "plot_point",
        "timestamp": 2,
        "description": "Evan meets Andy and they explore a creepy old toy store. Evan buys a dusty old can of 'Monster Blood'.",
        "participants": ["evan_ross", "andy"]
    },
    {
        "id": "evt_growing",
        "name": "The Slime Grows",
        "type": "escalation",
        "timestamp": 3,
        "description": "The Monster Blood starts growing uncontrollably after being exposed to air and dog saliva. It consumes everything in its path, including the twin bullies.",
        "participants": ["evan_ross", "andy", "monster_blood"]
    },
    {
        "id": "evt_climax",
        "name": "Confronting Sarabeth",
        "type": "climax",
        "timestamp": 4,
        "description": "The black cat reveals itself to be Sarabeth, an evil witch who cursed the Monster Blood. In the ensuing struggle, the giant Monster Blood consumes Sarabeth, shrinking back down as her magic is destroyed.",
        "participants": ["evan_ross", "andy", "aunt_kathryn", "sarabeth", "monster_blood"]
    }
]

locations = [
    {
        "id": "loc_kathryn_house",
        "name": "Aunt Kathryn's House",
        "type": "Residence",
        "description": "A dark, dusty, and eerie house in Atlanta. It feels unwelcoming and holds many secrets."
    },
    {
        "id": "loc_toy_store",
        "name": "Wagners Novelties & Sundries",
        "type": "Shop",
        "description": "A strange, run-down toy shop in town where the can of Monster Blood is found."
    }
]

# Write Agents
agents_dir = examples_dir / "agents_and_entities"
for key, data in agents.items():
    if "main" in data:
        with open(agents_dir / f"{key}.character_main.toml", "wb") as f:
            tomli_w.dump(data["main"], f)
    if "physical" in data:
        with open(agents_dir / f"{key}.character_physical.toml", "wb") as f:
            tomli_w.dump(data["physical"], f)
    if "psychology" in data:
        with open(agents_dir / f"{key}.character_psychology.toml", "wb") as f:
            tomli_w.dump(data["psychology"], f)

# Write Events
rules_dir = examples_dir / "dynamics_and_rules"
for idx, evt in enumerate(events):
    with open(rules_dir / f"plot_{idx:02d}.event.toml", "wb") as f:
        tomli_w.dump(evt, f)

# Write Locations
lore_dir = examples_dir / "world_and_lore"
for idx, loc in enumerate(locations):
    with open(lore_dir / f"loc_{idx:02d}.location.toml", "wb") as f:
        tomli_w.dump(loc, f)

# Copy the story
story_dir = base_dir / "data" / "stories"
source_txt = base_dir / "tmp" / "monster_blood.txt"
shutil.copy(source_txt, story_dir / "monster_blood.md")

print("Generated all files successfully.")
