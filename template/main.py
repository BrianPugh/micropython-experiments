import uprofiler


@uprofiler.profile
def main():
    pass


if __name__ == "__main__":
    main()
    uprofiler.print_results()
