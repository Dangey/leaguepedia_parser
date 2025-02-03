from dataclasses import dataclass

@dataclass
class LeaguepediaMatch:
    matchId: str

    startDT: str
    matchDay: int
    bestOf: int
    winner: str

    teams: list

    overviewPage: str

@dataclass
class LeaguepediaMatchTeam:
    id: int
    name: str
    score: int
    isWinner: bool

def transmute_match(match: dict) -> LeaguepediaMatch:
    winnerId = match["Winner"]
    return LeaguepediaMatch(
        matchId=match["MatchId"],
        startDT=match["DateTime UTC"],
        matchDay=match["MatchDay"],
        bestOf=match["BestOf"],
        winner=winnerId,
        teams=[
            LeaguepediaMatchTeam(
                id=1,
                name=match["Team1"],
                score=match["Team1Score"],
                isWinner=(winnerId == "1"),
            ),
            LeaguepediaMatchTeam(
                id=2,
                name=match["Team2"],
                score=match["Team2Score"],
                isWinner=(winnerId == "2"),
            ),
        ],
        overviewPage=match["OverviewPage"],
    )