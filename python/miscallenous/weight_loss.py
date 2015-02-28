# Enter your code here. Read input from STDIN. Print output to STDOUT
def weight_loss_leaderboard(arr):
    maps = {} # country code to dictionary of user_ids (dict of dicts)

    for i in range(len(arr)):
        country_code = arr[i][0]
        user_id = int(arr[i][1])
        weigh_in = float(arr[i][2])

        if country_code not in maps:
            # create key for that country_code
            maps[country_code] = {'weight_loss': 0}
            maps[country_code]['users'] = {}
            maps[country_code]['users'][user_id] = {}
            maps[country_code]['users'][user_id]['first_weigh_in'] = weigh_in
            maps[country_code]['users'][user_id]['weight_loss'] = 0
        else:
            if user_id not in maps[country_code]['users']:
                maps[country_code]['users'][user_id] = {}
                maps[country_code]['users'][user_id]['first_weigh_in'] = weigh_in
                maps[country_code]['users'][user_id]['weight_loss'] = 0
            else:
                maps[country_code]['users'][user_id]['last_weigh_in'] = weigh_in
                maps[country_code]['users'][user_id]['weight_loss'] = maps[country_code]['users'][user_id]['first_weigh_in'] - weigh_in

            total_weight_loss = 0
            for user_id in maps[country_code]['users']:
                total_weight_loss += maps[country_code]['users'][user_id]['weight_loss']

            maps[country_code]['weight_loss'] = total_weight_loss / len(maps[country_code]['users'])

    # return maps
        for country_code in sorted(maps):
            print "%s: %.1f," % (country_code, maps[country_code]['weight_loss']),
        print

import fileinput
inputs = []
for line in fileinput.input():
    input = line.rstrip().split(',')
    inputs.append(input)
print weight_loss_leaderboard(inputs)
