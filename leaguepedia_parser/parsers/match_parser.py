from typing import List
from leaguepedia_parser.site.leaguepedia import leaguepedia
from leaguepedia_parser.transmuters.field_names import match_fields
from leaguepedia_parser.transmuters.match import (
    transmute_match,
    LeaguepediaMatch,
)


def get_matches(tournament_overview_page=None, **kwargs) -> List[LeaguepediaMatch]:
    """Returns the list of games played in a tournament.

    Returns basic information about all games played in a tournament.

    Args:
        tournament_overview_page: tournament overview page, acquired from get_tournaments().

    Returns:
        A list of LolGame with basic game information.
    """

    matches = leaguepedia.query(
        tables="MatchSchedule",
        fields=", ".join(match_fields),
        where=f"MatchSchedule.OverviewPage ='{tournament_overview_page}'",
        order_by="MatchSchedule.DateTime_UTC",
        **kwargs,
    )

    return [transmute_match(match) for match in matches]