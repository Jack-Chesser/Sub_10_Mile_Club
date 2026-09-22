from espn_api.football import League
import json

league_id = 972786611
year = 2026

swid = "{DD283D64-C631-4EB2-83BA-6FA62B4B7391}"
espn_s2 = "AEAf84ASEZzei+09Y7K2Dxd2NgtYD9iRx7me7FTlkFEzCBg/p5FWr6ivvwrkz3MF2uUpwJRD2e9GugXGNPl0R9gM0nktSuW6jEif62KZlmVX0t6O858eQxMQcgBsLMKcEVqk8dXIiv59nvZecS3LDT6QTnIHVLn1hY4qY3vL8W1hZuG+f+BOuKB4/xnkRVwsZfKYl9nto7/+b2gb5rdE/oft0gkMfy9ScVcMBgLASHOlqPvHsfHB2opZpUME9/yNlr91hveEm1DWIBddFIqnPo+4"

league = League(
    league_id=league_id,
    year=year,
    swid=swid,
    espn_s2=espn_s2
)

data = {
    "teams": [
        {
            "name": team.team_name,
            "owners": team.owners,         
            "wins": team.wins,
            "losses": team.losses,
            "points_for": team.points_for,
            "points_against": team.points_against
        }
        for team in league.teams
    ]
}

with open("fantasy_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Fantasy data updated!")
