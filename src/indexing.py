from livedoor_news_search import LivedoorNewsSearch
from os import listdir, path

PATH = "text/"


def get_subdirs(path):
    subdirs = []
    for x in listdir(path):
        if not x.endswith('.txt'):
            subdirs.append(x)
    return subdirs


def get_filenames(path):
    labels = []
    for y in listdir(path):
        if not y.startswith('LICENSE'):
            labels.append(y)
    return labels


def main():
    lns = LivedoorNewsSearch()

    for d in get_subdirs(PATH):
        for fn in get_filenames(PATH+d):
            with open(path.join(PATH + d + "/" + fn), "r") as f:
                source = f.read()
                lns.addDocument(d, fn, source)


if __name__ == "__main__":
    main()
