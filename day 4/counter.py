
def Progress_days(dias):
    progress = 1
    counter = 0

    for day in dias:
        if progress < len(dias):
            if day < dias[progress]:
                counter += 1
        else:
            break
        progress += 1
         
    return counter

if(__name__ == "__main__"):
    Progress_days()