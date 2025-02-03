from dataclasses import dataclass

@dataclass
class LeaguepediaMatch:
    matchId: str

    startDT: str
    matchDay: int
    bestOf: int

    teams: list

    overviewPage: str

@dataclass
class LeaguepediaMatchTeam:
    id: int
    name: str
    score: int
    isWinner: bool

def transmute_match(match: dict) -> LeaguepediaMatch:
    teamOne = match["Team1"]
    teamTwo = match["Team2"]
    winner = match["Winner"]
    return LeaguepediaMatch(
        matchId=match["MatchId"],
        startDT=match["DateTime UTC"],
        matchDay=match["MatchDay"],
        bestOf=match["BestOf"],
        teams=[
            LeaguepediaMatchTeam(
                id=1,
                name=teamOne,
                score=match["Team1Score"],
                isWinner=(winner == teamOne),
            ),
            LeaguepediaMatchTeam(
                id=2,
                name=teamTwo,
                score=match["Team2Score"],
                isWinner=(winner == teamTwo),
            ),
        ],
        overviewPage=match["OverviewPage"],
    )