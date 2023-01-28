import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%d-%m-%Y %H:%M:%S')

def team_one(shuffled_players):

    if len(shuffled_players) <= 3:
        logging.error("No need to shuffle teams less than 3")
        return
    elif len(shuffled_players) == 4:
        one = shuffled_players[0:2]
        dash = "- "
        one_dash = [dash + x for x in one]
        team_one = '\n'.join(one_dash)
        logging.info("Teams have been sorted")
        print(f'{team_one}')
        return team_one
    else:
        one = shuffled_players[0:3]
        dash = "- "
        one_dash = [dash + x for x in one]
        team_one = '\n'.join(one_dash)
        logging.info("Teams have been sorted")
        logging.info(f'{team_one}')

    return team_one

def team_two(shuffled_players):

    if len(shuffled_players) <= 3:
        logging.error("No need to shuffle teams less than 3")
        return
    elif len(shuffled_players) == 4:
        two = shuffled_players[2:5]
        dash = "- "
        two_dash = [dash + x for x in two]
        team_two = '\n'.join(two_dash)
        logging.info("Teams have been sorted!")
        print(f'{team_two}')
        return team_two
    else:
        two = shuffled_players[3:7]
        dash = "- "
        two_dash = [dash + x for x in two]
        team_two = '\n'.join(two_dash)
        logging.info("Teams have been sorted!")
        print(f'{team_two}')

    return team_two