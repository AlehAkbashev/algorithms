troom, tcond = map(int, input().split())
mode = input()


def final_temp(temproom, tempcond, regime):
    if temproom == tempcond or regime == 'fan':
        return temproom
    elif regime == 'auto':
        return tempcond
    elif temproom > tempcond:
        if regime == 'freeze':
            return tempcond
        elif regime == 'heat':
            return temproom
    elif temproom < tempcond:
        if regime == 'freeze':
            return temproom
        elif regime == 'heat':
            return tempcond


print(final_temp(troom, tcond, mode))
