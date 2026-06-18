def main():
    angleMap = {}
    ang = 0
    angleMap[12] = ang

    for i in range(1, 12):
        ang += 30
        angleMap[i] = ang

    print(angleMap)


if __name__ == "__main__":
    main()
