if __name__ == "__main__":
    volumes = [0, 4, 8, 12, 16, 20, 24, 28, 31, 35, 39, 43, 47, 52, 56, 60, 64, 68, 72, 76, 80, 83, 87, 91, 95, 100]
    gaps = []
    for i in range(1, len(volumes)):
        gaps += [volumes[i]-volumes[i-1]]
    new_volumes = []
    initial_volume = 0
    for i in range(len(gaps)):
        new_volumes += [initial_volume]
        initial_volume += gaps[i]
    new_volumes += [initial_volume]
    initial_volume += gaps[i]
    print(volumes==new_volumes)