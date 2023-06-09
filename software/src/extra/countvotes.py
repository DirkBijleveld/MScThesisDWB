from software.src.util.filefinder import find_csv
from software.src.util.readutil import read


def main():
    clean = read(find_csv(9, clean=True))

    votes = clean.iloc[:, 7:]
    vote_count = votes.count()
    vote_count = vote_count.sum()
    print(vote_count)
    print(len(votes.columns))
if __name__ == "__main__":
    main()