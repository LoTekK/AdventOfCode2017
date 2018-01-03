import utils


with utils.get_input(21) as f:
    pattern = '.#./..#/###'
    input = [i.strip() for i in f.readlines()]
    rules2 = [i for i in input if len(i.split(' => ')[0].split('/')) == 2]
    rules3 = [i for i in input if len(i.split(' => ')[0].split('/')) == 3]
    print(rules2)
    print(rules3)
