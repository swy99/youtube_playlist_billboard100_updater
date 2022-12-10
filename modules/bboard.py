import billboard

def getchart(compact=True):
    chart = billboard.ChartData('hot-100')
    songs = chart[:]
    res = list(map(lambda song: [song.title, song.artist, song.artist + ' - ' + song.title], songs))
    if compact:
        res = list(map(lambda x: x[2], res))
    return res

def test():
    chart = getchart()
    print(chart[0:5])

if __name__ == "__main__":
    test()