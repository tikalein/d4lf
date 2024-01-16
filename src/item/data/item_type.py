from enum import Enum


# The values will be overwritte depending on which language is loaded
class ItemType(Enum):
    Amulet = "amulet"
    Axe = "axe"
    Axe2H = "two-handed axe"
    Boots = "boots"
    Bow = "bow"
    ChestArmor = "chest armor"
    Crossbow2H = "crossbow"
    Dagger = "dagger"
    Elixir = "elixir"
    Focus = "focus"
    Gloves = "gloves"
    Helm = "helm"
    Legs = "pants"
    Mace = "mace"
    Mace2H = "two-handed mace"
    OffHandTotem = "totem"
    Polearm = "polearm"
    Ring = "ring"
    Scythe = "scythe"
    Scythe2H = "two-handed scythe"
    Shield = "shield"
    Staff = "staff"
    Sword = "sword"
    Sword2H = "two-handed sword"
    Tome = "tome"
    Wand = "wand"
    # Custom Types
    Material = "material"
    Sigil = "sigil"
