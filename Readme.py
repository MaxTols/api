    import requests

    heroes = ["Hulk", "Captain America", "Thanos"]

    def max_intelligence(heroes_list):
        url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
        responses = requests.get(url)
        response = responses.json()
        hero_intelligence = dict()

        for hero in response:
            if hero["name"] in heroes_list:
                hero_intelligence[hero["name"]] = hero["powerstats"]["intelligence"]

        print(f'Самый умный из данных героев {max(hero_intelligence, key=hero_intelligence.get)}!')

    if __name__ == '__main__':
        max_intelligence(heroes)