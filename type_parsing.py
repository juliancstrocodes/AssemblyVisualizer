def parse_types(current: str):

    segments = []

    # loop through every character in current string
    for j in range(0, len(current)):

        c = current[j]

        if c == "," or c == "(" or c == ")":
            segments.append(".")
            continue

            # check if current is a minus sign (leading to new digit)
        if c == "-":
            segments.append([c])
            continue

        # check ic current is a non-alphanumeric character
        if not c.isalnum():
            continue

        # check if current is a digit
        if c.isdigit():
            # check if last subarray is an int
            try:
                if (segments[-1][-1]).isdigit() or (segments[-1][-1]) == "-":
                    segments[-1].append(c)
                else:
                    segments.append([c])
            except IndexError:
                segments.append([c])

            continue

        if c.isalpha():
            # check if last subarray is alphabetical
            try:
                if (segments[-1][-1]).isalpha():
                    segments[-1].append(c)
                else:
                    segments.append([c])
            except IndexError:
                segments.append([c])

            continue

    result = []
    for index, segment in enumerate(segments):
        if segment == "." and segments[index - 1] == ".":
            result.append(None)
            continue
        elif segment == "." and segments[index - 1] != ".":
            continue

        s = "".join(segment)
        if len(segment) != 0:
            result.append(s)

    return result
