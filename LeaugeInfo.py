from sleeper_wrapper import League
import json
from pathlib import Path

website_dir = Path(__file__).resolve().parent / "Foosball-Website"
website_dir.mkdir(parents=True, exist_ok=True)

national_foosball_league = League(1389389903917219840)

national_foosball_users = national_foosball_league.get_users()


national_foosball_rosters = national_foosball_league.get_rosters()


national_foosball_standings = national_foosball_league.get_standings(national_foosball_rosters, national_foosball_users)

national_foosball_standings_dict = []

rank = 0
for user in national_foosball_standings:
    rank += 1
    national_foosball_standings_dict.append({"rank": rank, "username": user[0], "wins": int(user[1]), "losses": int(user[2]), "points": int(user[3])})

filename = website_dir / "national_foosball_standings.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(national_foosball_standings_dict, file, indent=4)

national_foosball_league_jv = League(1391257937703358465)

national_foosball_users_jv = national_foosball_league_jv.get_users()

national_foosball_rosters_jv = national_foosball_league_jv.get_rosters()

national_foosball_standings_jv = national_foosball_league_jv.get_standings(national_foosball_rosters_jv, national_foosball_users_jv)

national_foosball_standings_dict_jv = []

rank = 0
for user in national_foosball_standings_jv:
    rank += 1
    national_foosball_standings_dict_jv.append({"rank": rank, "username": user[0], "wins": int(user[1]), "losses": int(user[2]), "points": int(user[3])})

filename = website_dir / "national_foosball_standings_jv.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(national_foosball_standings_dict_jv, file, indent=4)