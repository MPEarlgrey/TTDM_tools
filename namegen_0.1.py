import math
import time
import random

# Name Group
human_first = [
    "Tyra", "Senna", "Sylas", "Lux", "Alexis", "Ashley", "Andrea"
]
human_last_1 = ["Iron", "Stone", "Wood", "Ground", "Mc"]
human_last_2 = ["Hammer", "Spear", "Axe", "Sword", "Cauldron", "Sun", "Moon", "Star", "Opal"]

elf_first = [
    "Aerosin", "Baerithryn", "Cameron", "Darthoridan", "Elandorr", "Faoraar", "Galaeron",
    "Halafarin", "Iyrandrar", "Jhaeros", "Keryth", "Lathai", "Marikoth", "Naertho",
    "Oslarelar", "Paeral", "Quastarte", "Rhaac'var", "Sudryl", "Tanyl", "Uthorim",
    "Vartan", "Wyrran", "Xhalh", "Yhendorn", "Zabbas"
]
elf_last_1 = ["Ere", "Daen", "Thar", "Dorn", "Lith", "Thil", "Vyr"]
elf_last_2 = ["aelo", "win", "riel"]

# Fetchling names
fetchling_first = [
    "Ahlos", "Brys", "Cyris", "Dushar", "Eshai", "Feyr", "Ghael", "Hadrin",
    "Ithys", "Jorren", "Kyss", "Leth", "Mirel", "Nyx", "Orrin", "Phael",
    "Qyra", "Riven", "Sable", "Teryn", "Umbra", "Vesh", "Wrynn", "Xerin",
    "Ysil", "Zev"
]
fetchling_last_1 = ["Shade", "Night", "Gloom", "Umbra", "Shadow", "Teneb", "Noct", "Murk", "Dusk"]
fetchling_last_2 = ["borne", "weaver", "stride", "veil", "song", "ward", "fell", "mark", "whisper"]

namegroups = {"human", "elf", "fetchling"}

# Name Generation
while True:
    input_name = input("Enter a name group (human, elf, fetchling) or 'exit' to quit: ").strip().lower()
    if input_name == "exit":
        print("Exiting the name generator.")
        break

    if input_name not in namegroups:
        print(f"Invalid name group '{input_name}'. Please choose from {sorted(namegroups)}.")
        continue

    if input_name == "human":
        print("Generating a human name...")
        time.sleep(1)
        n1 = random.choice(human_first)
        n21 = random.choice(human_last_1)
        n22 = random.choice(human_last_2)
        print("name:", n1, n21 + n22)

    elif input_name == "elf":
        print("Generating an elf name...")
        time.sleep(1)
        n1 = random.choice(elf_first)
        n21 = random.choice(elf_last_1)
        n22 = random.choice(elf_last_2)
        print("name:", n1, n21 + n22)

    elif input_name == "fetchling":
        print("Generating a fetchling name...")
        time.sleep(1)
        n1 = random.choice(fetchling_first)
        n21 = random.choice(fetchling_last_1)
        n22 = random.choice(fetchling_last_2)
        print("name:", n1, n21 + n22)

