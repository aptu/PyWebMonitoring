#!/usr/bin/python

# Takes the input file of the format:
# -- the 1 column is Unix time
# -- the 2 column is 200s count
# -- the 3 column is 404s count
# -- the 2 column is 500s count

# Produces a temp.tsv file with:
# -- the 1 column is Unix time
# -- the 2 column is 200s rps
# -- the 3 column is 404s rps
# -- the 2 column is 500s rps

import collections

Datapoint = collections.namedtuple('Datapoint', ['time', 'r200', 'r404', 'r500'])


if __name__ == "__main__":

    #list of datapoints
    points_10s = []
    with open("stats.tsv", "r") as f:
        for row in f:
            time, r200, r404, r500 = map(int, row.strip().split('\t'))
            points_10s.append(Datapoint(time=time, r200=r200, r404=r404, r500=r500))

    points_1m = []
    for k in range(5, len(points_10s), 6):
        i = k - 6 if k > 5 else 0
        point = Datapoint(time=points_10s[k].time, r200=(points_10s[k].r200-points_10s[i].r200)/60,
                  r404=(points_10s[k].r404-points_10s[i].r404)/60,
                  r500=(points_10s[k].r500-points_10s[i].r500)/60)
        points_1m.append(point)



    with open("temp.tsv", "w") as outfile:
        for p in points_1m:
            outfile.write("%d\t%d\t%d\t%d\n" % (p.time, p.r200, p.r404, p.r500))

