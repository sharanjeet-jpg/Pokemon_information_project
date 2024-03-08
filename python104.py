import requests

while True:
    pokemon = input("Enter the name of the pokemon you want to find:\t")
    pokemon = pokemon.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()
        print(f"Name is\t\t{data['name']}")
        print("Abilities:------------------\n")

        for index, ability in enumerate(data['abilities']):
            ability_name = ability['ability']['name']
            print(f"{index + 1}. {ability_name}")
            print("*" * 20)

            ability_url = f"https://pokeapi.co/api/v2/ability/{ability_name}"
            ability_req = requests.get(ability_url)

            if ability_req.status_code == 200:
                ability_data = ability_req.json()
                for effect in ability_data['effect_entries']:
                    if effect['language']['name'] == 'en':
                        print(effect['effect'])
                    print("\n")
        print(f"Weight:\t\t{data['weight']}")
    else:
        print("Pokemon not found")

    response = input("Do you want to continue [Y]/[N]:\t")
    response = response.lower()

    if response != 'y':
        break
